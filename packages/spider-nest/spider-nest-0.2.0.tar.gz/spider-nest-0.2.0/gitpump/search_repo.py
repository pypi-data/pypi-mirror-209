from github import (
    GithubObject,
    Repository,
)

from .base import (
    Base,
)

from .describe_repo import (
    DescribeRepo,
)

from .constants import (
    Status,
    RESULT_LIMIT_PER_SEARCH,
    T_NAME_LEN,
)

from .util import (
    _wait_rate_limit,
    format_time_cost,
    _format_dt,
    _repo_info,
)

from logging import Logger
from threading import Thread, Lock
from datetime import datetime, timedelta

import threading
import time
import json
import math
import sys
import os


class SearchRepo(Base):
    # repo_extractor is a callback method to extract inforamtion from github.Repository
    # method definition: def _repo_info(repo: Repository) -> {}:
    def __init__(self, token: str, logger: Logger = None, repo_extractor = None):
        super().__init__(token=token, logger=logger)
        self._repo_extractor = repo_extractor
        if repo_extractor is None:
            self._repo_extractor = _repo_info

    def _check_star_range(self, star_from:int, star_to:int=sys.maxsize):
        if star_to < star_from:
            msg = "Illegal star range: [{:d}, {:d}]".format(star_from, star_to)
            self._print_err(msg)
            return False
        if star_from < 300:
            self._print_warn("Warning! There are too many repositories within low star range,"
                             " you will miss them dur to limit of search result")
        return True

    # search repositories with stars in [star_from, star_to]
    # callback is a callback method to output repos
    # callback method definition: def pop_repos(repos:[])
    # progress_bar is a callback method to display progress
    # progress_bar method definition: def show_progress(title:str, current:int, total:int)
    def search_by_star_range(self, star_from: int, star_to: int, callback=None, progress_bar=None) -> int:
        if not self._check_star_range(star_from, star_to):
            return 1

        status, total_count, first_repo = self.search_by_query(query="stars:"+str(star_from)+".."+str(star_to-1),
                                                               sort='stars',
                                                               order='asc',
                                                               callback=callback,
                                                               )

        star_gap = star_to - star_from
        if status == Status.RESULT_EXCEED_LIMIT and star_gap > 1:
            star_increment = int(star_gap/2.0)
            msg = "Search step by step, increment:{:d}".format(star_increment)
            self._print_info(msg)
            n = star_to
            while n > star_from:
                n = n - star_increment
                s_to = n+star_increment
                if n < star_from:
                    n = star_from
                star_increment = self.search_by_star_range(star_from=n,
                                                           star_to=s_to,
                                                           callback=callback,
                                                           )
                self._call_progressbar(progress_bar, "Searching repos", s_to-n, star_gap)

        self._call_progressbar(progress_bar, "Searching repos", star_gap, star_gap)

        return star_gap

    # search repositories with stars in [star_from, infinity]
    # callback is a callback method to output repos
    # callback method definition: def pop_repos(repos:[])
    # progress_bar is a callback method to display progress
    # progress_bar method definition: def show_progress(title:str, current:int, total:int)
    def search_by_star_begin(self, star_from: int, callback=None, progress_bar=None):
        self._check_star_range(star_from)

        status, total_count, first_repo = self.search_by_query(query="stars:>=350000",
                                                               sort='stars',
                                                               order='desc',
                                                               callback=callback,
                                                               )
        star_to = star_from
        if total_count > 0:
            star_to = first_repo["stargazers_count"] + 5000
        return self.search_by_star_range(star_from=star_from,
                                         star_to=star_to,
                                         callback=callback,
                                         progress_bar=progress_bar,
                                         )

    def search_by_query(self,
                        query:str,
                        sort=GithubObject.NotSet,
                        order=GithubObject.NotSet,
                        callback=None,
                        ):
        thread_name = threading.current_thread().name[:T_NAME_LEN]
        msg = "[{:s}] Search repos by query:{:s}, {:s}"\
            .format(thread_name, query, time.strftime('%Y:%m:%d %H:%M:%S', time.localtime(int(time.time()))))
        self._print_info(msg)
        start = time.time()

        repo_num = 0
        repo_total_count = 0
        try:
            rate_limit = self._g.get_rate_limit()
            _wait_rate_limit(rate_limit=rate_limit, show_me=True, logger=self._logger)

            repositories = self._g.search_repositories(query=query, sort=sort, order=order)

            repos = []
            for repo in repositories:
                _wait_rate_limit(rate_limit=rate_limit, logger=self._logger)
                repo_data = self._repo_extractor(repo)
                if repo_num == 0:
                    repo_total_count = repositories.totalCount
                    if repo_total_count >= RESULT_LIMIT_PER_SEARCH:
                        msg = "[{:s}] Search result count {:d} exceeds limit {:d}"\
                            .format(thread_name, repo_total_count, RESULT_LIMIT_PER_SEARCH)
                        self._print_info(msg)
                        return Status(Status.RESULT_EXCEED_LIMIT, msg), repo_total_count, repo_data
                    else:
                        msg = "[{:s}] Search result count {:d}".format(thread_name, repo_total_count)
                        self._print_info(msg)

                repo_num = repo_num + 1
                repos.append(repo_data)
                # if repo_num % 100 == 0:
                #     self._print_info("[{:s}] {:d} repos founds".format(thread_name, repo_num))

            end = time.time()
            self._print_info("[{:s}] Output {:d} repos, time cost: {:s}"
                             .format(thread_name, len(repos), format_time_cost(end - start)))
        except Exception as e:
            self._print_err("Failed to search repos by query {:s}, error: {}".format(query, e))
            return Status(Status.FAILED, "search failed, error: {}".format(e)), repo_total_count, {}

        if callback:
            try:
                callback(repos)
            except Exception as e:
                self._print_err("Callback error for query {:s}, error: {}".format(query, e))
                return Status(Status.FAILED, "callback failed, error: {}".format(e)), repo_total_count, {}

        first_repo = {}
        if len(repos) > 0:
            first_repo = repos[0]
        return Status(Status.SUCCESS, "search success"), repo_total_count, first_repo


class ParallelSearchRepo(Base):
    def __init__(self, tokens: [], batch_size: int = 1000, logger: Logger = None):
        token = ""
        if len(tokens) > 0:
            token = tokens[len(tokens)-1]
        super().__init__(token=token, logger=logger)
        self._tokens = tokens
        self._batch_size = batch_size
        self._repo_info_fn = _repo_info
        self._output_repo_fn = self.__output_repos

        self._repos_buffer = []
        self._lock_repos_buffer = Lock()
        self._repos_count = 0
        self._output_path = ""

    def _reset(self):
        self._repos_buffer = []
        self._repos_count = 0

    def __dump_file(self, target_folder: str, repos: list):
        if len(repos) == 0 or len(target_folder) == 0:
            return

        file_name = "star_{:d}_to_{:d}.json"\
            .format(repos[0]["stargazers_count"], repos[len(repos) - 1]["stargazers_count"])
        full_name = os.path.join(target_folder, file_name)
        try:
            with open(full_name, 'w', encoding='utf-8') as f:
                content = {
                    "repo_count": len(repos),
                    "repositories": repos,
                }
                json.dump(obj=content, fp=f, indent=2, ensure_ascii=False)
            msg = "Dump file:{:s} for {:d} repos".format(full_name, len(repos))
            self._print_info(msg)
        except Exception as e:
            msg = "Failed to dump:{:s}, err: {}".format(full_name, e)
            self._print_err(msg)

    def __output_repos(self, repo_list: list):
        self._lock_repos_buffer.acquire()
        self._repos_buffer.extend(repo_list)
        self._repos_count = self._repos_count + len(repo_list)
        if len(self._repos_buffer) >= self._batch_size:
            def sort_key(element):
                return element["stargazers_count"]

            self._repos_buffer.sort(key=sort_key)
            self.__dump_file(self._output_path, self._repos_buffer)
            self._print_info("{:d} repos have been dumped".format(self._repos_count))
            self._repos_buffer.clear()
        self._lock_repos_buffer.release()

    def _split_range(self, star_from: int, star_to: int) -> []:
        if star_from < 0 or star_from > star_to:
            msg = "Illegal star range [{:d}, {:d}]".format(star_from, star_to)
            self._print_err(msg)
            return []

        star_ranges = []
        step = 1
        next_from = star_from
        next_to = next_from + step
        while next_to < star_to:
            step = (2 ** (int(math.log(next_to))))*max(1, math.ceil(next_to/5000))
            if step < 1:
                step = 1

            next_to = next_from + step
            if next_to > star_to:
                next_to = star_to

            new_range = [next_from, next_to]
            star_ranges.append(new_range)
            next_from = next_to

        self._print_info("Total ranges: {:d}".format(len(star_ranges)))
        return star_ranges

    # output_repos is a callback func like: def output_repos(repo_list: list)
    def _worker_search_range(self, token: str, star_range: [], output_repos):
        start = time.time()
        thread_name = threading.current_thread().name[:T_NAME_LEN]
        try:
            msg = "[{:s}] Search repos in range {}".format(thread_name, star_range)
            self._print_info(msg)

            searcher = SearchRepo(token=token,
                                  logger=self._logger,
                                  repo_extractor=self._repo_info_fn)
            searcher.search_by_star_range(star_from=star_range[0],
                                          star_to=star_range[1],
                                          callback=output_repos)
        except Exception as e:
            self._print_err("[{:s}] Failed to search in range {}, error: {}".format(thread_name, star_range, e))

        end = time.time()
        msg = "[{:s}] Search repos in range {} finished, time cost: {:s}"\
            .format(thread_name, star_range, format_time_cost(end - start))
        self._print_info(msg)
        self._wait_continue()

    def parallel_search_repos(self,
                              star_from: int,
                              star_to: int,
                              output_folder: str,
                              time_out: float = 60 * 60 * 4,
                              progress_bar=None,
                              ):
        """Search repos by star range.
                    :param star_from: star range begin
                    :param star_to: star range end, set to -1 to search [star_from, ∞]
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

        # find the top 1 repo star as the star_to value
        if star_to < 0:
            searcher = SearchRepo(token=self._tokens[0],
                                  logger=self._logger,
                                  repo_extractor=self._repo_info_fn)
            status, total_count, first_repo = searcher.search_by_query(query="stars:>=350000",
                                                                       sort='stars',
                                                                       order='desc')
            star_to = first_repo["stargazers_count"] + 5000

        start = time.time()
        star_ranges = self._split_range(star_from, star_to)
        self._print_info("Search ranges: {:d} {}".format(len(star_ranges), star_ranges))

        self._reset()
        self._output_path = output_folder

        threads_alive = []
        thread_num = len(self._tokens)
        self._stop_all = False
        idle_tokens = set()
        lock_tokens = Lock()
        for tk in self._tokens:
            idle_tokens.add(tk)

        ranges_count = len(star_ranges)
        thread_stat = {"done_count": 0}
        def done_handler(threads_done:[]):
            for t in threads_done:
                self._print_info("Searching thread '{:s}' done".format(t.name[:T_NAME_LEN]))
                lock_tokens.acquire()
                idle_tokens.add(t.name)
                lock_tokens.release()
                thread_stat["done_count"] = thread_stat["done_count"] + 1
                if thread_stat["done_count"] > ranges_count:
                    thread_stat["done_count"] = ranges_count
                self._call_progressbar(progress_bar, "Searching repos", thread_stat["done_count"], ranges_count)

        while len(star_ranges) > 0:
            if self._stop_all:
                break

            token = None
            lock_tokens.acquire()
            if len(idle_tokens) > 0:
                token = idle_tokens.pop()
            lock_tokens.release()
            if token:
                one_range = star_ranges[0]
                star_ranges = star_ranges[1:]
                t = Thread(target=self._worker_search_range,
                           name=token,
                           args=(token, one_range, self._output_repo_fn,))
                threads_alive.append(t)
                t.start()
                self._print_info("Create new thread '{:s}' for range: {}, ranges left: {:d}"
                                 .format(t.name[:T_NAME_LEN], one_range, len(star_ranges)))

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

        if len(self._repos_buffer) > 0:
            self.__dump_file(output_folder, self._repos_buffer)

        end = time.time()
        self._print_info("Finish search repos in star range [{:d}, {:d}], totally found {:d} repos, time cost: {:s}"
                         .format(star_from, star_to, self._repos_count, format_time_cost(end - start)))


class SearchRepoStarHistory(ParallelSearchRepo):
    def __init__(self, tokens: [], logger: Logger = None):
        super().__init__(tokens=tokens, logger=logger)
        self._repo_info_fn = self.__repo_info
        self._output_repo_fn = self.__output_repos

    def __repo_info(self, repo: Repository) -> {}:
        repo_info = {}
        repo_info["full_name"] = repo.full_name
        repo_info["stargazers_count"] = repo.stargazers_count
        repo_info["html_url"] = repo.html_url
        return repo_info

    def __output_repos(self, repo_list: list):
        self._lock_repos_buffer.acquire()
        self._repos_buffer.extend(repo_list)
        self._repos_count = self._repos_count + len(repo_list)
        self._lock_repos_buffer.release()

    def _parallel_get_star_history(self,
                                   repos: list,
                                   rising_stars: int,
                                   from_date: datetime,
                                   time_out: float = 60 * 60 * 4):
        start = time.time()

        repo_his = []
        lock_his = Lock()

        def _worker_get_history(token: str, repo: {}):
            des = DescribeRepo(token=token, logger=self._logger)
            star_his = des.get_star_history(repo["full_name"], from_date=from_date)
            if len(star_his) >= rising_stars:
                lock_his.acquire()
                repo_his.append(des.format_repo_history(repo, star_his))
                lock_his.release()
                self._print_info("Repo '{:s}' is hot! {:d} stars gained from {:s}"
                                 .format(repo["full_name"], len(star_his), _format_dt(from_date)))

        threads_alive = []
        thread_num = len(self._tokens)
        self._stop_all = False
        idle_tokens = set()
        lock_tokens = Lock()
        for tk in self._tokens:
            idle_tokens.add(tk)

        def done_handler(threads_done:[]):
            for t in threads_done:
                self._print_info("History thread '{:s}' done".format(t.name[:T_NAME_LEN]))
                lock_tokens.acquire()
                idle_tokens.add(t.name)
                lock_tokens.release()

        while len(repos) > 0:
            if self._stop_all:
                break

            token = None
            lock_tokens.acquire()
            if len(idle_tokens) > 0:
                token = idle_tokens.pop()
            lock_tokens.release()
            if token:
                one_repo = repos[0]
                repos = repos[1:]
                t = Thread(target=_worker_get_history,
                           name=token,
                           args=(token, one_repo, ))
                threads_alive.append(t)
                t.start()
                self._print_info("Create new thread '{:s}' for repo history: {}, repos left: {:d}"
                                 .format(t.name[:T_NAME_LEN], one_repo["full_name"], len(repos)))

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
        self._print_info("Finish get star history of {:d} repos, time cost: {:s}"
                         .format(self._repos_count, format_time_cost(end - start)))
        return repo_his

    def search_hot_repos(self, output_folder: str, star_from: int, rising_stars: int, duration: timedelta):
        start = time.time()
        self.parallel_search_repos(star_from=star_from,
                                   star_to=-1,
                                   output_folder="",
                                   )
        self._print_info("Finish search repos from star > {:d}, totally found {:d} repos"
                         .format(star_from, self._repos_count,))

        def sort_key(element):
            return element["stargazers_count"]
        self._repos_buffer.sort(key=sort_key)

        from_date = datetime.now() - duration
        repo_his = self._parallel_get_star_history(self._repos_buffer,
                                                   rising_stars=rising_stars,
                                                   from_date=from_date)

        end = time.time()
        self._print_info("Finish search hot repos, totally found {:d} repos, time cost: {:s}"
                         .format(self._repos_count, format_time_cost(end - start)))

        if len(repo_his) > 0:
            file_name = "star_history_gt{:d}_rising{:d}_from{:s}.json" \
                .format(star_from, rising_stars, _format_dt(from_date))
            full_name = os.path.join(output_folder, file_name)
            try:
                with open(full_name, 'w', encoding='utf-8') as f:
                    json.dump(obj=repo_his, fp=f, indent=2, ensure_ascii=False)
                msg = "Dump star history file: {:s} for {:d} repos".format(full_name, len(repo_his))
                self._print_info(msg)
            except Exception as e:
                msg = "Failed to dump star history file: {:s}, err: {}".format(full_name, e)
                self._print_err(msg)

        return repo_his