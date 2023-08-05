import math

from github import (
    PaginatedList,
    ContentFile,
    License,
    GitRelease,
)

from .base import (
    Base,
)

from .constants import (
    Status,
    CONTRIBUTOR_NUM,
    T_NAME_LEN,
)

from .util import (
    _wait_rate_limit,
    _repo_info,
    _user_info,
    _format_dt,
    format_time_cost,
    get_http_request,
    construct_repo_folder,
    download_file,
)

from web2markdown import (
   DumpWebsite,
)

from retry import retry
from logging import Logger
from threading import Thread
from datetime import  datetime

import time
import json
import os


class DescribeRepo(Base):
    def __init__(self, token: str, logger: Logger = None):
        super().__init__(token=token, logger=logger)

    @retry(tries=2, delay=10)
    def _get_users(self, users: PaginatedList):
        user_list = []
        try:
            index = 0
            for user in users:
                user_info = _user_info(user)
                user_list.append(user_info)
                index = index + 1
                if index >= CONTRIBUTOR_NUM:
                    break
        except Exception as e:
            self._print_err("Failed to get users, error: {}".format(e))

        return user_list

    def _get_license(self, lic: License):
        lic_info = {}
        try:
            lic_info["name"] = lic.name
            lic_info["description"] = lic.description
            lic_info["permissions"] = lic.permissions
            lic_info["conditions"] = lic.conditions
            lic_info["limitations"] = lic.limitations
        except Exception as e:
            self._print_err("Failed to get license, error: {}".format(e))

        return lic_info

    @retry(tries=2, delay=10)
    def _get_file(self, content: ContentFile):
        file_info = {}
        try:
            file_info["name"] = content.name
            file_info["download_url"] = content.download_url
            # file_info["size"] = content.size
            if content.license:
                file_info["license"] = self._get_license(content.license)
        except Exception as e:
            self._print_err("Failed to get file object, error: {}".format(e))

        return file_info

    @retry(tries=2, delay=10)
    def _get_release(self, release: GitRelease):
        release_info = {}
        try:
            release_info["title"] = release.title
            release_info["tag_name"] = release.tag_name
            release_info["target_commitish"] = release.target_commitish
            release_info["published_at"] = _format_dt(release.published_at)
            release_info["url"] = release.url
        except Exception as e:
            self._print_err("Failed to get release, error: {}".format(e))

        return release_info

    def get_repo(self, repo_full_name: str):
        try:
            rate_limit = self._g.get_rate_limit()
            _wait_rate_limit(rate_limit=rate_limit, core_remain_alert=5, show_me=True, logger=self._logger)
            repo = self._g.get_repo(full_name_or_id=repo_full_name)
            return Status(Status.SUCCESS), repo
        except Exception as e:
            msg = "Failed to get repo {:s} object, error: {}".format(repo_full_name, e)
            self._print_err(msg)
            return Status(Status.FAILED, msg), None

    def get_detail(self, repo_full_name: str):
        msg = "Describe repo by name:{:s}, {:s}".format(repo_full_name,
                                                        time.strftime('%Y:%m:%d %H:%M:%S',
                                                                      time.localtime(int(time.time()))))
        self._print_info(msg)

        start = time.time()
        materials = {}
        status, repo = self.get_repo(repo_full_name=repo_full_name)
        if not status.OK():
            return status, {}

        # # this property is too slow in search_repo, postpone to here
        # materials["watchers_count"] = repo.subscribers_count

        self._print_info("Get repo {} object, time cost: {:s}"
                         .format(repo_full_name, format_time_cost(time.time()-start)))
        m_t = time.time()

        rate_limit = self._g.get_rate_limit()
        try:
            _wait_rate_limit(rate_limit=rate_limit, core_remain_alert=15, show_me=True, logger=self._logger)
            lic = repo.get_license()
            materials["license"] = self._get_file(lic)
        except Exception as e:
            self._print_err("Failed to get license of repo {:s}, error: {}".format(repo_full_name, e))

        self._print_info("Get repo {} license, time cost: {:s}"
                         .format(repo_full_name, format_time_cost(time.time() - m_t)))
        m_t = time.time()

        try:
            _wait_rate_limit(rate_limit=rate_limit, core_remain_alert=15, show_me=True, logger=self._logger)
            readme = repo.get_readme()
            materials["readme"] = self._get_file(readme)
        except Exception as e:
            self._print_err("Failed to get readme of repo {:s}, error: {}".format(repo_full_name, e))

        self._print_info("Get repo {} readme, time cost: {:s}"
                         .format(repo_full_name, format_time_cost(time.time() - m_t)))
        m_t = time.time()

        try:
            _wait_rate_limit(rate_limit=rate_limit, core_remain_alert=10, show_me=True, logger=self._logger)
            langs = repo.get_languages()
            materials["languages"] = langs
        except Exception as e:
            self._print_err("Failed to get languages of repo {:s}, error: {}".format(repo_full_name, e))

        self._print_info("Get repo {} language, time cost: {:s}"
                         .format(repo_full_name, format_time_cost(time.time() - m_t)))
        m_t = time.time()

        try:
            _wait_rate_limit(rate_limit=rate_limit, core_remain_alert=10, show_me=True, logger=self._logger)
            release = repo.get_latest_release()
            materials["latest_release"] = self._get_release(release)
        except Exception as e:
            self._print_err("Failed to get latest release of repo {:s}, error: {}".format(repo_full_name, e))

        self._print_info("Get repo {} latest release, time cost: {:s}"
                         .format(repo_full_name, format_time_cost(time.time() - m_t)))
        m_t = time.time()

        try:
            _wait_rate_limit(rate_limit=rate_limit,
                             core_remain_alert=CONTRIBUTOR_NUM*10+5,
                             show_me=True,
                             logger=self._logger)
            contributors = repo.get_contributors()
            materials["contributors"] = {
                "total_count": contributors.totalCount,
                "users": self._get_users(contributors),
            }
        except Exception as e:
            self._print_err("Failed to get contributors, error: {}".format(e))

        self._print_info("Get repo {} contributors, time cost: {:s}"
                         .format(repo_full_name, format_time_cost(time.time() - m_t)))

        end = time.time()
        msg = "Fetch repo {:s} detail time cost: {:s}".format(repo_full_name, format_time_cost(end - start))
        self._print_info(msg)
        return Status(Status.SUCCESS, "describe repo success"), materials

    def _download_wiki(self, url: str, target_path: str):
        start = time.time()
        try:
            dw = DumpWebsite(logger=self._logger)
            md, redirect_url = dw.dump_html(url=url,
                                            ignore_header_footer=True,
                                            skip_redirect=True)
            if (not md) or (len(md) == 0):
                return

            # hardcode to trim the unnecessary content
            wiki_begin = "Clone this wiki locally"
            poz = md.find(wiki_begin)
            if poz >= 0:
                poz = poz + len(wiki_begin)
                md = md[poz:].lstrip("\n")
            if len(md) < 10:
                return

            with open(target_path, 'w', encoding='utf-8') as f:
                f.write(md)

            end = time.time()
            msg = "Finish parse wiki page {:s} to {:s}, time cost:{:s} seconds"\
                .format(url, target_path, format_time_cost(end - start))
            self._print_info(msg)
        except Exception as e:
            msg = "Failed to parse wiki page {:s}, error: {}".format(url, e)
            self._print_err(msg)

    def download_summary(self, output_folder: str, repo_x):
        try:
            start = time.time()
            if isinstance(repo_x, str):
                status, repo = self.get_repo(repo_x)
                if not status.OK():
                    self._print_err("Failed to get repo {:s}, error: {:s}".format(repo_x, status.message))
                    return
            elif isinstance(repo_x, dict):
                repo = repo_x
            else:
                self._print_err("Not a valid repo object")
                return

            if "full_name" not in repo:
                self._print_err("Not a valid repo object: {}".format(repo))
                return

            repo_folder, summary_file_path = construct_repo_folder(repo["full_name"],
                                                                   output_folder,
                                                                   logger=self._logger)
            if len(repo_folder) == 0 or len(summary_file_path) == 0:
                return

            os.makedirs(name=repo_folder, exist_ok=True)

            # detail
            summary = repo
            status, detail = self.get_detail(repo_full_name=repo["full_name"])
            if not status.OK():
                return
            summary.update(detail)

            # store summary
            with open(summary_file_path, 'w', encoding='utf-8') as f:
                json.dump(obj=summary, fp=f, indent=2, ensure_ascii=False)

            end = time.time()
            self._print_info("Summary of {} downloaded, time cost: {:s}"
                             .format(repo_x, format_time_cost(end - start)))
            return summary
        except Exception as e:
            self._print_err("Failed to get summary of {}, error: {}".format(repo_x, e))
            return {}

    def download_attachment(self, output_folder: str, repo: {}):
        if (repo is None) or ("full_name" not in repo):
            self._print_err("Invalid repo object: {}".format(repo))
            return

        try:
            start = time.time()
            repo_folder, summary_file_path = construct_repo_folder(repo["full_name"],
                                                                   output_folder,
                                                                   logger=self._logger)

            # store wiki
            if "html_url" in repo and ("has_wiki" in repo and repo["has_wiki"]):
                wiki_url = repo["html_url"] + "/wiki"
                wiki_file_path = os.path.join(repo_folder, "wiki.md")
                self._download_wiki(wiki_url, wiki_file_path)

            # store readme
            if "readme" in repo and "download_url" in repo["readme"]:
                readme_url = repo["readme"]["download_url"]
                download_file(readme_url, repo_folder, logger=self._logger)

            # store license
            if "license" in repo and "download_url" in repo["license"]:
                license_url = repo["license"]["download_url"]
                download_file(license_url, repo_folder, logger=self._logger)

            end = time.time()
            self._print_info("Attachment of {:s} downloaded, time cost: {:s}"
                             .format(repo["full_name"], format_time_cost(end - start)))
        except Exception as e:
            self._print_err("Failed to get attachment of {:s}".format(repo["full_name"]))

    def format_repo_history(self, repo: {}, star_history: []):
        repo_his = repo
        history = {}
        for dt_str in star_history:
            date_str = dt_str[:dt_str.find("T")]
            if date_str in history:
                history[date_str] = history[date_str] + 1
            else:
                history[date_str] = 1
        repo_his["star_history"] = history
        return repo_his

    def get_star_history(self, repo_full_name: str, from_date: datetime = None):
        start = time.time()

        per_page = 100
        url = "https://api.github.com/repos/{:s}/stargazers?per_page={:d}".format(repo_full_name, per_page)
        header = {
            "Authorization": "token " + self._token,
            "Accept": "application/vnd.github.v3.star+json",
        }
        res = []

        def append_stars(stars: list) -> bool:
            stop = False
            for s in reversed(stars):
                dt_str = s['starred_at']
                if from_date:
                    dt = datetime.strptime(dt_str, '%Y-%m-%dT%H:%M:%SZ')
                    if dt < from_date:
                        stop = True
                        break
                res.append(dt_str)
            return stop

        rate_limit = self._g.get_rate_limit()
        _wait_rate_limit(rate_limit=rate_limit,
                         core_remain_alert=5,
                         show_me=True,
                         logger=self._logger)

        resp = get_http_request(url=url, logger=self._logger, headers=header, timeout=20)
        if resp is None:
            self._print_err("Failed to fetch stargazers: {:s}".format(url))
            return []

        if "last" in resp.links:
            target_url = resp.links["last"]["url"]
            while target_url is not None:
                _wait_rate_limit(rate_limit=rate_limit,
                                 core_remain_alert=5,
                                 show_me=True,
                                 logger=self._logger)

                resp = get_http_request(url=target_url, logger=self._logger, headers=header, timeout=20)
                if resp is None:
                    self._print_err("Failed to fetch stargazers: {:s}".format(target_url))
                    break

                stars = json.loads(resp.content)
                stop = append_stars(stars)
                if stop:
                    break

                if "prev" in resp.links:
                    target_url = resp.links["prev"]["url"]
                else:
                    target_url = None
        else:
            stars = json.loads(resp.content)
            append_stars(stars)

        end = time.time()
        self._print_info("Get {:d} stars of repo '{:s}' from date {:s}, time cost: {:s}"
                         .format(len(res), repo_full_name,
                                 from_date.strftime('%Y-%m-%d %H:%M:%S'),
                                 format_time_cost(end - start)))
        return res



class ParallelDownloadRepos(Base):
    def __init__(self, tokens: [], logger: Logger = None):
        token = ""
        if len(tokens) > 0:
            token = tokens[len(tokens)-1]
        super().__init__(token=token, logger=logger)
        self._tokens = tokens

    def _collect_repos_base_info(self, folder: str):
        repo_list = []
        for parent, dirnames, filenames in os.walk(folder):
            if parent is folder:
                for filename in filenames:
                    ext = os.path.splitext(filename)
                    if len(ext) != 2 or ext[1] != ".json":
                        continue
                    fullpath = os.path.join(parent, filename)
                    with open(fullpath, encoding='utf-8') as f:
                        content = json.load(f)
                        if "repositories" in content.keys():
                            repos = content["repositories"]
                            self._print_info("Found {:d} repos in {:s}".format(len(repos), fullpath))
                            repo_list.extend(repos)
                break
        return repo_list

    def _ignore_exist_repos(self, repos: list, parent_folder: str) -> list:
        result_list = []
        exist_count = 0
        for repo in repos:
            repo_folder, repo_file_path = construct_repo_folder(repo["full_name"], parent_folder)
            if os.path.exists(repo_file_path):
                exist_count = exist_count + 1
                continue

            result_list.append(repo)
        self._print_info("{:d} repos already exist, no need to download".format(exist_count))
        return result_list


    def _worker_download_repos(self, token: str, repo_list: list, output_folder: str, ):
        dr = DescribeRepo(token=token, logger=self._logger)
        for repo in repo_list:
            if self._stop_all:
                break

            summary = dr.download_summary(output_folder=output_folder, repo_x=repo)
            dr.download_attachment(output_folder=output_folder, repo=summary)

        self._print_info("Thread {:s} finished after downloading {:d} repos".format(token[:T_NAME_LEN], len(repo_list)))
        self._wait_continue()

    def parallel_download_by_search_result(self,
                                           output_folder: str,
                                           time_out: float = 60 * 60 * 4,
                                           progress_bar=None,
                                           ):
        """Download repos by multi-threads.
            :param output_folder: target folder to store files
            :param time_out: timeout value to force stop all threads, units: second.
            :param progress_bar: def show_progress(title:str, current:int, total:int).
            """
        all_repos = self._collect_repos_base_info(output_folder)
        repo_list = self._ignore_exist_repos(all_repos, output_folder)
        if len(repo_list) == 0:
            self._print_info("No repo need to be downloaded")
            return

        return self._parallel_download(output_folder=output_folder,
                                       repo_list=repo_list,
                                       time_out=time_out,
                                       progress_bar=progress_bar)

    def parallel_download_by_list(self,
                                  output_folder: str,
                                  repo_list: list,
                                  time_out: float = 60 * 60 * 4,
                                  progress_bar=None,
                                  ):
        if len(self._tokens) == 0:
            self._print_warn("Github token list is empty, skip the work")
            return

        repos = []
        dr = DescribeRepo(token=self._tokens[0], logger=self._logger)
        for repo_full_name in repo_list:
            status, repo = dr.get_repo(repo_full_name)
            if not status.OK():
                self._print_err("Failed to get repo by name '{:s}'".format(repo_full_name))
                return

            info = _repo_info(repo)
            repos.append(info)

        if len(repos) == 0:
            self._print_info("No repo need to be downloaded")
            return

        return self._parallel_download(output_folder=output_folder,
                                       repo_list=repos,
                                       time_out=time_out,
                                       progress_bar=progress_bar)

    def _parallel_download(self,
                           output_folder: str,
                           repo_list: list,
                           time_out: float = 60 * 60 * 4,
                           progress_bar=None,
                           ):
        """Download repos by multi-threads.
            :param repo_list: a repo list of str or dict
            :param output_folder: target folder to store files
            :param time_out: timeout value to force stop all threads, units: second.
            :param progress_bar: def show_progress(title:str, current:int, total:int).
            """
        if len(self._tokens) == 0:
            self._print_warn("Github token list is empty, skip the work")
            return
        if time_out <= 0:
            self._print_warn("Timeout value is less or equal to 0, skip the work")
            return

        start = time.time()

        threads_alive = []
        thread_num = len(self._tokens)
        self._stop_all = False
        batch = int(len(repo_list)/thread_num)
        if batch < 1:
            batch = 1
        if batch > 10:
            batch = 10
        self._print_info("{:d} repos, {:d} for each batch and {:d} threads".format(len(repo_list), batch, thread_num))

        idle_tokens = set()
        for tk in self._tokens:
            idle_tokens.add(tk)

        total_count = len(repo_list)
        stat = {"done_count": 0}

        def done_handler(threads_done: []):
            for t in threads_done:
                idle_tokens.add(t.name)
                stat["done_count"] = stat["done_count"] + batch
                if stat["done_count"] > total_count:
                    stat["done_count"] = total_count
                self._print_info("{:d} repos have been downloaded".format(stat["done_count"]))
                self._call_progressbar(progress_bar, "Downloading repos", stat["done_count"], total_count)

        while len(repo_list) > 0:
            if self._stop_all:
                break

            if len(idle_tokens) > 0:
                token = idle_tokens.pop()
                batch_repos = repo_list[0:batch]
                repo_list = repo_list[batch:]

                t = Thread(target=self._worker_download_repos,
                           name=token,
                           args=(token, batch_repos, output_folder,))
                threads_alive.append(t)
                t.start()
                self._print_info("Create new thread '{:s}' for {:d} repos, {:d} repos left"
                                 .format(t.name[:T_NAME_LEN], len(batch_repos), len(repo_list)))

            if len(threads_alive) >= thread_num:
                threads_alive, threads_done = self._wait_thread(threads=threads_alive,
                                                                time_start=start,
                                                                time_out=time_out)
                done_handler(threads_done)

        while len(threads_alive) > 0:
            threads_alive, threads_done = self._wait_thread(threads=threads_alive,
                                                            time_start=start,
                                                            time_out=time_out)
            done_handler(threads_done)

        end = time.time()
        time_cost = end - start
        msg = "{:d} repos downloaded, time cost: {:s}".format(stat["done_count"], format_time_cost(time_cost))
        if time_cost > time_out:
            self._print_info("Canceled, " + msg)
        else:
            self._print_info("Finished, " + msg)
