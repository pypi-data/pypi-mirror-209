import datetime
import time
import os
import json

from pyquery import PyQuery
from logging import Logger
from threading import Thread

from .base import (
    Base,
)

from .util import (
    get_http_request,
    format_time_cost,
)


class FetchTrending(Base):
    def __init__(self, logger: Logger = None):
        super().__init__(token="", logger=logger)

    def fetch_trending(self, time_scope, language) -> []:
        valid_scope = ["daily", "weekly", "monthly"]
        if not (time_scope in valid_scope):
            self._print_err("Invalid timescope {:s}, the value must be in {}".format(time_scope, valid_scope))
            return []

        start = time.time()
        msg = "Get trending of {:s} for {:s}".format(language, time_scope)
        self._print_info(msg)

        if language == "Any":
            url = 'https://github.com/trending?since={:s}'.format(time_scope)
        else:
            url = 'https://github.com/trending/{:s}?since={:s}'.format(language, time_scope)

        trending_list = []
        try:
            resp = get_http_request(url, self._logger)
            if resp is None:
                return []

            content = PyQuery(resp.content)
            items = content('div.Box article.Box-row')

            for item in items:
                item_info = {}
                pq = PyQuery(item)
                item_info["full_name"] = pq(".lh-condensed a").text().replace(' ', '')
                item_info["url"] = "https://github.com" + pq(".lh-condensed a").attr("href")
                item_info["description"] = pq("p.col-9").text()

                trending_list.append(item_info)
        except Exception as e:
            self._print_err("Failed to parse trending page, error: {}".format(e))

        end = time.time()
        self._print_info("Fetch trending({:s}, {:s}) finished, time cost: {:s}"
                         .format(time_scope, language, format_time_cost(end - start)))
        return trending_list

    def _download_trending(self, output_path: str, time_scope: str, language: str):
        trending_list = self.fetch_trending(language=language, time_scope=time_scope)
        content = {
            "created_time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "language": language,
            "time_scope": time_scope,
            "trending": trending_list,
        }

        trending_path = os.path.join(output_path, "trending")
        os.makedirs(name=trending_path, exist_ok=True)

        scope_path = os.path.join(trending_path, time_scope)
        os.makedirs(name=scope_path, exist_ok=True)

        language_path = os.path.join(scope_path, language)
        os.makedirs(name=language_path, exist_ok=True)

        full_name = os.path.join(language_path, datetime.date.today().strftime("%Y-%m-%d") + ".json")
        with open(full_name, 'w', encoding='utf-8') as f:
            json.dump(obj=content, fp=f, indent=2, ensure_ascii=False)

        self._print_info("Download trending({:s}, {:s}) to file: {:s}"
                         .format(time_scope, language, full_name))
        self._wait_continue()

    def parallel_download_trending(self,
                                   output_folder: str,
                                   time_scopes: [],
                                   languages: [],
                                   thread_num: int = 10,
                                   time_out: float = 60*60,
                                   progress_bar=None,
                                   ):
        """Fetch trending by multi-threads.
               :param output_folder: target folder to store files
               :param time_scopes: Any/Daily/Weekly/Monthly
               :param languages: programing language list
               :param thread_num: number of threads
               :param time_out: timeout value to force stop all threads, units: second.
               :param progress_bar: def show_progress(title:str, current:int, total:int).
               """
        self._print_info("Prepare to fetch trending in {:d} time scopes and {:d} languages"
                         .format(len(time_scopes), len(languages)))
        start = time.time()
        total = len(time_scopes)*len(languages)
        current = 0
        threads_alive = []
        self._stop_all = False
        for time_scope in time_scopes:
            for language in languages:
                if self._stop_all:
                    break

                current = current + 1
                self._call_progressbar(progress_bar, "Fetching trending", current, total)

                t = Thread(target=self._download_trending, args=(output_folder, time_scope, language,))
                threads_alive.append(t)
                t.start()
                self._print_info("Create new thread '{:s}' for trending({:s}, {:s})"
                                 .format(t.name, time_scope, language))
                if len(threads_alive) >= thread_num:
                    threads_alive, threads_done = self._wait_thread(threads=threads_alive,
                                                                    time_start=start,
                                                                    time_out=time_out)

        self._wait_thread(threads=threads_alive,
                          time_start=start,
                          time_out=time_out,
                          wait_all=True)
        self._call_progressbar(progress_bar, "Fetching trending", total, total)

        end = time.time()
        self._print_info("Finish to fetch trending in {:d} time scopes and {:d} languages, time cost: {:s}"
                         .format(len(time_scopes), len(languages), format_time_cost(end - start)))
