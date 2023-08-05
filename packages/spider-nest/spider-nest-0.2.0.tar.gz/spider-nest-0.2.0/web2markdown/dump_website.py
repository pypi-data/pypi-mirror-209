from .base import (
    Base,
)

from .html2text.html2text_wrapper import (
    HTML2TextWrapper,
)

from .util import (
    get_http_request,
    get_http_header,
    format_time_cost,
)

from pyquery import PyQuery
from logging import Logger
from threading import Thread, Lock
from urllib.parse import urlparse
from .usp.tree import sitemap_tree_for_homepage
from selenium import webdriver

import tldextract
import urllib.parse
import mimetypes
import time
import json
import re
import os


class DumpWebsite(Base):
    def __init__(self, logger: Logger = None):
        super().__init__(logger=logger)
        self.__reset()

    def __reset(self):
        self._max_accept_size = 1024 * 1024
        self._root_site = ""
        self._done_list = set()
        self._lock_done = Lock()
        self._links_pool = set()
        self._lock_links = Lock()
        self._blacklist = set()
        self._whitelist = set()

    def _add_to_links_pool(self, links: list):
        if (not links) or (len(links) == 0):
            return
        self._lock_links.acquire()
        count = 0
        for link in links:
            if link in self._links_pool:
                continue
            self._links_pool.add(link)
            count = count + 1
        self._lock_links.release()
        self._print_info("Append {:d} links to the pool".format(count))

    def _pop_links_pool(self):
        ele = None
        self._lock_links.acquire()
        count = len(self._links_pool)
        if count > 0:
            ele = self._links_pool.pop()
        self._lock_links.release()
        self._print_info("{:d} links left in the pool, {:d} links have been viewed"
                         .format(count, len(self._done_list)))
        return ele

    def _get_links_pool(self) -> list:
        p = list(self._links_pool)
        p.sort()
        return p

    def __set_root_site(self, url:str):
        # set the root site for the first time
        if len(self._root_site) == 0:
            tld = tldextract.extract(url)
            self._root_site = "{:s}.{:s}".format(tld.domain, tld.suffix)
            self._print_info("Set root site '{:s}' of '{:s}'".format(self._root_site, url))
            if len(tld.subdomain) > 0 and tld.subdomain != "www":
                up = urlparse(url)
                self._whitelist.add(up.netloc + up.path)

    def __set_whitelist(self, white_list: list):
        if white_list:
            for w in white_list:
                if isinstance(w, str):
                    self._whitelist.add(w)

    def __set_blacklist(self, black_list: list):
        if black_list:
            for b in black_list:
                if isinstance(b, str):
                    self._blacklist.add(b)

    def __is_valid_url(self, url: str) -> bool:
        # exclude black list
        up = urlparse(url)
        if up.netloc in self._blacklist:
            return False

        # allows subdomain
        if len(self._root_site) > 0:
            is_white = False if len(self._whitelist) > 0 else True
            for white in self._whitelist:
                if (up.netloc + up.path).startswith(white):
                    is_white = True
                    break
            if not is_white:
                return False

            tld = tldextract.extract(url)
            domain = "{:s}.{:s}".format(tld.domain, tld.suffix)
            if domain != self._root_site:
                return False
        return True

    def _put_url_done(self, url:str):
        self._lock_done.acquire()
        self._done_list.add(url)
        self._lock_done.release()

    def _is_url_done(self, url: str) -> bool:
        is_done = False
        self._lock_done.acquire()
        if url in self._done_list:
            is_done = True
        self._lock_done.release()
        return is_done

    def done_list(self) -> list:
        return list(self._done_list)

    def _is_mimetext(self, url: str) -> bool:
        up = urlparse(url)
        if not up.scheme.startswith('http'):
            return False

        if len(up.path) == 0:
            return True

        tail = up.path[up.path.rfind("/", 0)+1:]
        tp = mimetypes.guess_type(tail)
        if tp[0] and not tp[0].startswith('text/'):
            return False
        return True

    def is_http_url(self, url: str) -> bool:
        try:
            up = urlparse(url)
            if not up.scheme.startswith('http'):
                return False
            return all([up.scheme, up.netloc])
        except:
            return False

    def _normalize_url(self, url:str) -> str:
        sla = url.rfind("/")
        tag = url.rfind("#")
        if sla < tag:
            url = url[:tag]

        v = url.strip(" ").replace("\n", "").replace("\r", "")
        return v

    def _download_page(self, url: str, use_driver: bool = False):
        if use_driver:
            try:
                option = webdriver.ChromeOptions()
                option.add_argument(argument='headless')  # run in background
                driver = webdriver.Chrome(options=option)
                driver.get(url)
                time.sleep(3)
                return driver.page_source, driver.current_url
            except Exception as e:
                self._print_err("Failed to download url '{}' by driver, error: {}".format(url, e))
                return None, url
        else:
            resp = get_http_request(url, self._logger)
            if resp is None:
                return None, url
            return resp.content, resp.url

    def dump_html(self, url: str, skip_redirect: bool = False):
        url = self._normalize_url(url)

        # sometimes the url is a huge download file, but recognized as a html address, don't download this file
        header = get_http_header(url)
        if header:
            content_type = header.get("Content-Type", None)
            if content_type and (not content_type.startswith("text")):
                self._print_warn("The url '{:s}' content type '{:s}' is not text type".format(url, content_type))
                return None, url

            content_size = header.get("Content-Length", None)
            if content_size and int(content_size) >= self._max_accept_size:
                self._print_err("The url '{:s}' content size '{:s}' is too large".format(content_size, url))
                return None, url

        # fetch the html page
        page_content, redirect_url =\
            self._download_page(url, use_driver = True if (len(self._root_site) == 0) else False)
        if page_content is None:
            return None, url

        # if the url is redirected, don't parse it
        if skip_redirect and redirect_url != url:
            self._print_warn("Wiki page '{:s}' was redirected to '{:s}', no need to parse".format(url, redirect_url))
            return None, url

        # redirect url by website
        if redirect_url and len(redirect_url) != 0:
            url = self._normalize_url(redirect_url)

        try:
            if (not page_content) or (len(page_content) == 0):
                self._print_warn("The url '{:s}' content is empty".format(url))
                return None, url

            self._print_info("Convert url '{:s}' to markdown".format(url))
            content = PyQuery(page_content)
            return content.html(), url
        except Exception as e:
            self._print_err("The url '{:s}' content is empty, error: {}".format(url, e))
            return None, url

    def convert_html_2_md(self, content: str, ignore_header_footer: bool = True):
        # convert html to md
        ignore_tags = []
        if ignore_header_footer:
            ignore_tags.append("head")
            ignore_tags.append("header")
            ignore_tags.append("footer")
        h2t = HTML2TextWrapper()
        h2t.ignore_tags(ignore_tags)
        md = h2t.handle(content)

        return md.rstrip("\n")

    def _find_links(self, md: str, parent_url: str) -> []:
        if not md:
            return []

        reg = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
        links = dict(reg.findall(md))
        ulinks = []
        for item in links:
            v = links[item]

            # relative url to absolute url
            if v.find("://") < 0:
                v = urllib.parse.urljoin(parent_url, v)

            if v == parent_url:
                continue

            # avoid duplicate url
            # convert tag url "cc/dd/#a" to "cc/dd/"
            v = self._normalize_url(v)
            if v in ulinks:
                continue

            # ignore non-text url such as jpg/png/tar/zip
            if not self._is_mimetext(v):
                continue

            # ignore url not in this site
            if not self.__is_valid_url(v):
                continue

            # ignore done
            if self._is_url_done(v):
                continue

            ulinks.append(v)

        self._print_info("Found {:d} links of url '{:s}'".format(len(ulinks), parent_url))
        return ulinks

    def _dump_and_store(self, url: str,
                        output_path: str,
                        ignore_header_footer: bool = True,
                        cut_after: str = "",
                        cut_before: str = "",
                        ):
        if self._is_mimetext(url):
            content, url = self.dump_html(url)
            if not content:
                return None, url
            file_name = "content.md"
            md = self.convert_html_2_md(content, ignore_header_footer=ignore_header_footer)
        else:
            self._print_warn("The url '{:s}' is not text type".format(url))
            return None, url

        md = self._cut_content(md, cut_after=cut_after, cut_before=cut_before)

        try:
            relative_path = url.replace("https:", "").replace("http:", "").lstrip("/")
            full_path = os.path.join(output_path, relative_path)
            os.makedirs(name=full_path, exist_ok=True)

            # no need to store if it exists
            file_path = os.path.join(full_path, file_name)
            if os.path.exists(file_path):
                return md, url
            with open(file_path, "w", encoding='utf-8') as f:
                f.write(md)
            self._print_info("Save url '{:s}' content to '{:s}'".format(url, file_path))

            # # for debug
            # file_path = os.path.join(full_path, "page.html")
            # with open(file_path, "w", encoding='utf-8') as f:
            #     f.write(content)
        except Exception as e:
            self._print_err("Failed to store url '{:s}' content, error: {}".format(url, e))

        return md, url

    def _cut_content(self, content: str, cut_after: str = None, cut_before: str = None):
        if content is None:
            return None
        try:
            if cut_after and len(cut_after) > 0:
                content = content[0: content.rfind(cut_after)]
            if cut_before and len(cut_before) > 0:
                content = content[content.find(cut_before):]
        except Exception as e:
            self._print_err("Failed to cut content: {}".format(e))
        return content

    def _store_and_find_links(self, url: str,
                              output_path: str,
                              ignore_header_footer: bool = True,
                              cut_after: str = "",
                              cut_before: str = "",
                              find_links: bool = True,
                              ) -> []:
        if not self.is_http_url(url):
            self._print_err("The url '{:s}' is not a http/https url".format(url))
            return []

        url = self._normalize_url(url)
        start = time.time()
        md, redirect_url = self._dump_and_store(url,
                                                output_path,
                                                ignore_header_footer=ignore_header_footer,
                                                cut_after=cut_after,
                                                cut_before=cut_before,
                                                )
        self._put_url_done(url)
        self._put_url_done(redirect_url)
        url = redirect_url

        if (not md) or len(md) == 0:
            end = time.time()
            self._print_info("The url '{:s}' content is empty, totally parsed {:d} url, time cost: {:s}"
                             .format(url, len(self._done_list), format_time_cost(end - start)))
            return []

        if not find_links:
            end = time.time()
            self._print_info("No need to find links for url '{:s}', totally parsed {:d} url, time cost: {:s}"
                             .format(url, len(self._done_list), format_time_cost(end - start)))
            return []

        self.__set_root_site(url)
        links = self._find_links(md, url)
        if (not links) or (len(links) == 0):
            end = time.time()
            self._print_info("The url '{:s}' has no sub links, totally parsed {:d} url, time cost: {:s}"
                             .format(url, len(self._done_list), format_time_cost(end - start)))
            return []

        end = time.time()
        self._print_info("{:d} sub links found for url '{:s}', totally parsed {:d} url, time cost: {:s}"
                         .format(len(links), url, len(self._done_list), format_time_cost(end - start)))
        return links

    def _get_sitemap(self, url: str) -> set:
        start = time.time()
        tree = sitemap_tree_for_homepage(url, logger=self._logger)
        sitemap = set()
        for page in tree.all_pages():
            sitemap.add(page.url)

        end = time.time()
        self._print_info("Finished searching sitemap, {:d} urls found, time cost: {:s}"
                         .format(len(sitemap), url, format_time_cost(end - start)))
        return sitemap

    def _worker_store_and_find_links(self, url: str,
                                     output_path: str,
                                     cut_after: str,
                                     cut_before: str,
                                     find_links: bool,
                                     ignore_header_footer: bool = True,
                                     ) -> []:
        links = self._store_and_find_links(url=url,
                                           output_path=output_path,
                                           cut_after=cut_after,
                                           cut_before=cut_before,
                                           find_links=find_links,
                                           ignore_header_footer=ignore_header_footer,
                                           )
        self._add_to_links_pool(links)
        self._wait_continue()

    def parallel_dump_website(self, url: str,
                              output_path: str,
                              thread_num: int = 16,
                              cut_after: str = "",
                              cut_before: str = "",
                              time_out: float = 60*60*4,
                              try_sitemap=False,
                              black_list: list = None,
                              white_list: list = None,
                              ignore_header_footer: bool = True,
                              ):
        """Fetch website pages by multi-threads.
            :param output_path: target folder to store markdown files
            :param url: URL of a website.
            :param thread_num: threads number.
            :param cut_after: use special string to remove unnecessary content after this string.
            :param cut_before: use special string to remove unnecessary content before this string.
            :param time_out: timeout value to force stop all threads, units: second.
            :param try_sitemap: fetch sitemap to get urls.
            :param black_list: black list will be excluded.
            """
        self.__reset()
        self.__set_blacklist(black_list)
        self.__set_whitelist(white_list)

        if not self.is_http_url(url):
            self._print_err("The website '{:s}' is not a http/https url".format(url))
            return []

        start = time.time()
        links = []
        if try_sitemap:
            links = list(self._get_sitemap(url))

        # if the website has no sitemap, use brute-force search
        find_link = True
        if len(links) == 0:
            links = self._store_and_find_links(url=url,
                                               output_path=output_path,
                                               ignore_header_footer=False,
                                               cut_after=cut_after,
                                               cut_before=cut_before,
                                               )
        else:
            find_link = False

        self._print_info("Seed urls: {:s}".format(json.dumps(links, indent=2)))

        threads_alive = []

        ######## strategy, each thread random pick an unique url
        self._add_to_links_pool(links)
        while True:
            if self._stop_all:
                break

            link = self._pop_links_pool()
            while link:
                if self._stop_all:
                    break
                if time.time() - start > time_out:
                    self._print_warn("Time out! break the loop")
                    break

                t = Thread(target=self._worker_store_and_find_links,
                           args=(link, output_path, cut_after, cut_before, find_link, ignore_header_footer))
                threads_alive.append(t)
                t.start()
                self._print_info("Create new thread '{:s}' for url '{:s}'".format(t.name, link))
                link = self._pop_links_pool()
                if len(threads_alive) >= thread_num:
                    threads_alive, threads_done = self._wait_thread(threads=threads_alive,
                                                                    time_start=start,
                                                                    time_out=time_out)
            self._wait_thread(threads=threads_alive,
                              time_start=start,
                              time_out=time_out,
                              wait_all=True)
            if len(self._links_pool) == 0:
                break
            if time.time() - start > time_out:
                self._print_warn("Time out! break the loop")
                break

        end = time.time()
        time_cost = end - start
        msg = "'{:s}', totally parsed {:d} url, time cost: {:s}"\
            .format(url, len(self._done_list), format_time_cost(time_cost))
        if time_cost > time_out:
            self._print_info("Canceled, " + msg)
            self._print_info("Unfinish links: {:s}".format(json.dumps(self._get_links_pool(), indent=2)))
        else:
            self._print_info("Finished, " + msg)
