import threading
from datetime import datetime

from github import (
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
    T_NAME_LEN,
)

from .util import (
    _wait_rate_limit,
    format_time_cost,
    _issue_info,
    construct_repo_folder,
    _repo_info,
)

from logging import Logger
from pyquery import PyQuery
from selenium import webdriver
from threading import Thread, Lock
from selenium.webdriver.common.by import By

import time
import json
import os


class IssueFilter:
    def __init__(self, from_date: datetime = None):
        self.from_date = from_date

class FetchIssues(Base):
    def __init__(self, token: str, logger: Logger = None, filter: IssueFilter = None):
        super().__init__(token=token, logger=logger)
        self._filter = filter

    def _get_issue(self, repo: Repository, number: int):
        try:
            rate_limit = self._g.get_rate_limit()
            _wait_rate_limit(rate_limit=rate_limit, core_remain_alert=50, show_me=True, logger=self._logger)
            issue = repo.get_issue(number)
            if issue:
                issue_info = _issue_info(issue)
                return issue_info
        except Exception as e:
            self._print_err("Failed to get issue object, error: {}".format(e))
        return None

    def get_discussion(self, repo_full_name: str, number: int):
        url = 'https://github.com/{:s}/discussions/{:d}'.format(repo_full_name, number)
        self._print_info("Get discussion: " + url)

        try:
            option = webdriver.ChromeOptions()
            option.add_argument(argument='headless')  # run in background
            driver = webdriver.Chrome(options=option)
            driver.get(url)

            # click all the "Show xx previous replies" buttons
            btns = driver.find_elements(By.CSS_SELECTOR, "button[data-disable-with='Loading more replies...']")
            for btn in btns:
                btn.click()

            # wait the page to expand until there is no "Show xx previous replies" buttons
            r = 0
            while ("Loading more replies..." in driver.page_source) and r <= 5:
                time.sleep(1)
                self._print_info("Wait more replies expand: " + url)
                r = r + 1

            def _init_comment_info():
                return {
                    "user": "",
                    "created_at": "",
                    "link": "",
                    "paragraphs": [],
                    "is_answer": False,
                }

            # parse content
            info = {}
            content = PyQuery(driver.page_source)
            info["number"] = number
            info["html_url"] = url
            bucket = content('div#discussion_bucket')
            info["title"] = bucket('h1.gh-header-title').text()
            groups = bucket('div.timeline-comment-group').not_('.discussion-nested-comment-group')
            group_list = []
            for g in groups:
                group_info = {"comments": []}
                cc = PyQuery(g)('div.edit-comment-hide')
                comment_info = _init_comment_info()
                for c in cc:
                    # header is author and datetime
                    h = PyQuery(c)('h1,h2,h3,h4,h5,h6.timeline-comment-header-text')
                    if h:
                        aa = PyQuery(h)('a')
                        created = []
                        for a in aa:
                            rt = PyQuery(a)('relative-time')
                            if rt:
                                created.append([PyQuery(rt).attr('datetime'), PyQuery(a).attr('href')])
                            else:
                                created.append([PyQuery(a).text(), PyQuery(a).attr('href')])
                        if len(created) > 0:
                            comment_info["user"] = created[0][0]
                        if len(created) > 1:
                            comment_info["created_at"] = created[1][0]
                            comment_info["link"] = created[1][1]
                            if "created_at" not in info:
                                info["created_at"] = comment_info["created_at"]

                    btn = PyQuery(c)("button[aria-label='Marked as answer']")
                    if btn:
                        comment_info["is_answer"] = True

                    # presentation is sentences
                    presentation = PyQuery(c)('table[role=presentation]')
                    if presentation:
                        pp = PyQuery(presentation)('code,p,ul,ol:not([hidden])')
                        for p in pp:
                            para = PyQuery(p)
                            # ignore quote
                            if para.parent().is_('blockquote'):
                                continue

                            if para.is_('ol'):
                                lis = PyQuery(para)('li')
                                id = 1
                                for li in lis:
                                    comment_info["paragraphs"].append("{:d}. {:s}".format(id, PyQuery(li).text()))
                                    id = id + 1
                            elif para.is_('ul'):
                                lis = para('li')
                                for li in lis:
                                    comment_info["paragraphs"].append("- {:s}".format(PyQuery(li).text()))
                            elif para.is_('code'):
                                if para.parent().is_('p'):
                                    continue
                                comment_info["paragraphs"].append("```{:s}```".format(para.text()))
                            else:
                                comment_info["paragraphs"].append(para.text())
                        group_info["comments"].append(comment_info)
                        comment_info = _init_comment_info()

                group_list.append(group_info)

            info["comments_history"] = group_list
            driver.quit()
            self._print_info("Finished: " + url)
            # no answers, skip
            if len(group_list) <= 1:
                return None

            return info
        except Exception as e:
            self._print_err("Failed to parse discussion page, error: {}".format(e))
            return None

    def get_discussions(self, repo_full_name: str, numbers: list):
        discussion_list = []
        for number in numbers:
            info = self.get_discussion(repo_full_name, number)
            if info:
                discussion_list.append(info)

        return discussion_list

    # deduce discussion numbers, not accurate
    def _deduce_discussion_numbers(self,
                                   issue_numbers: list,
                                   pull_numbers: list,
                                   ):
        max1 = 0
        max2 = 0
        min1 = 0
        min2 = 0
        if len(issue_numbers) > 0:
            max1 = max(issue_numbers)
            min1 = min(issue_numbers)
        if len(pull_numbers) > 0:
            max2 = max(pull_numbers)
            min2 = min(pull_numbers)
        if max1 < max2:
            max1 = max2
        if min1 > min2:
            min1 = min2

        discussion_numbers = []
        for i in range(min1, max1):
            if (i not in issue_numbers) and (i not in pull_numbers):
                discussion_numbers.append(i)
        discussion_numbers.sort(reverse=True)
        return discussion_numbers

    # filter number by self._filter.from_date
    # return three number list: issue_numbers, pull_numbers, discussion_numbers
    def _get_issue_pull_numbers(self, repo: Repository, progress_bar=None):
        repo_full_name = repo.full_name
        msg = "Get numbers of issues of repo:{:s}, {:s}".format(repo_full_name,
                                                                time.strftime('%Y:%m:%d %H:%M:%S',
                                                                              time.localtime(int(time.time()))))
        self._print_info(msg)
        start = time.time()
        try:
            rate_limit = self._g.get_rate_limit()
            _wait_rate_limit(rate_limit=rate_limit, core_remain_alert=10, show_me=True, logger=self._logger)
            issues = repo.get_issues(
                state="all",
                sort="created",
                direction="desc",
            )
            self._print_info("Repo '{:s}' total number count:{:d}".format(repo_full_name, issues.totalCount))

            count = 0
            total_count = issues.totalCount
            issues_numbers = []
            pull_numbers = []
            try:
                for issue in issues:
                    count = count + 1
                    if count % 100 == 0:
                        self._call_progressbar(progress_bar,
                                               "Get issues number list of repo '{:s}'".format(repo_full_name),
                                               count,
                                               total_count)
                    if count % 1000 == 0:
                        self._print_info("Received {:d} of {:d} numbers".format(count, total_count))

                    # filter by date
                    if self._filter and self._filter.from_date:
                        if issue.created_at < self._filter.from_date:
                            break

                    if repo_full_name + "/pull" in issue.html_url:
                        pull_numbers.append(issue.number)
                        continue
                    issues_numbers.append(issue.number)
                self._call_progressbar(progress_bar,
                                       "Get issues number list of repo '{:s}'".format(repo_full_name),
                                       total_count,
                                       total_count)
            except Exception as e:
                self._print_err("Failed to iterate issues, {:d} of {:d} received, error: {}"
                                .format(count, total_count, e))

            issues_numbers.sort(reverse=True)
            pull_numbers.sort(reverse=True)
            discussion_numbers = self._deduce_discussion_numbers(issues_numbers, pull_numbers)

            end = time.time()
            self._print_info("Get issues numbers time cost: {:s}".format(format_time_cost(end - start)))
            return Status(Status.SUCCESS, "search success"), issues_numbers, pull_numbers, discussion_numbers
        except Exception as e:
            self._print_err("Failed to get numbers of issues, error: {}".format(e))
            return Status(Status.FAILED, "failed to get numbers of issues: {:s}".format(repo_full_name)), [], [], []

    # progress_bar is a callback method to display progress
    # progress_bar method definition: def show_progress(title:str, current:int, total:int, logger:logging.logger)
    def get_issues_numbers(self, repo_full_name: str, progress_bar=None):
        desc = DescribeRepo(self._token, logger=self._logger)
        status, repo = desc.get_repo(repo_full_name)
        if not status.OK():
            self._print_err(status.message)
            return status, [], []

        status, i_numbers, p_numbers, d_numbers = self._get_issue_pull_numbers(repo, progress_bar=progress_bar)
        if not status.OK():
            self._print_err(status.message)
        return i_numbers, p_numbers, d_numbers

    # callback is a callback method to output issues
    # callback method definition: def pop_issue(issue_info:{})
    # progress_bar is a callback method to display progress
    # progress_bar method definition: def show_progress(title:str, current:int, total:int, logger:logging.logger)
    def fetch_issues(self, repo_full_name: str, numbers: list, callback=None, progress_bar=None):
        msg = "Fetch issues of repo:{:s}, {:s}".format(repo_full_name, time.strftime('%Y:%m:%d %H:%M:%S',
                                                                                     time.localtime(int(time.time()))))
        self._print_info(msg)

        desc = DescribeRepo(self._token, logger=self._logger)
        status, repo = desc.get_repo(repo_full_name)
        if not status.OK():
            self._print_info(status.message)
            return status, []

        try:
            count = 0
            total_count = len(numbers)
            issues_list = []
            for number in numbers:
                count = count + 1
                if progress_bar:
                    progress_bar("Fetch issues", count, total_count, self._logger)
                if count % 10 == 0:
                    self._print_info("{:d} of {:d} issues have been parsed".format(count, len(numbers)))

                issue_info = self._get_issue(repo, number)
                if not issue_info:
                    continue

                if callback:
                    callback(issue_info)
        except Exception as e:
            self._print_err("Failed to fetch issues, error: {}".format(e))
            return Status(Status.FAILED, "failed to fetch issues"), []

        return Status(Status.SUCCESS, "search success"), issues_list


class ParallelFetchIssues(Base):
    def __init__(self, tokens: [], logger: Logger = None, filter: IssueFilter = None):
        token = ""
        if len(tokens) > 0:
            token = tokens[len(tokens)-1]
        super().__init__(token=token, logger=logger)
        self._tokens = tokens
        self._filter = filter

    def _dump_file(self, target_folder: str, issues_list: list):
        try:
            def sort_key(element):
                return element['number']

            issues_list.sort(key=sort_key)
            file_name = "{:d}_to_{:d}.json".format(issues_list[0]["number"],
                                                   issues_list[len(issues_list) - 1]["number"])
            file_full_name = os.path.join(target_folder, file_name)
            with open(file_full_name, 'w', encoding='utf-8') as f:
                content = {
                    "count": len(issues_list),
                    "items": issues_list,
                }
                json.dump(obj=content, fp=f, indent=2, ensure_ascii=False)
            msg = "Dump file:{:s} for {:d} issues/discussions".format(file_full_name, len(issues_list))
            self._print_info(msg)
        except Exception as e:
            msg = "Failed to dump file: {}".format(e)
            self._print_err(msg)

    def _parallel_fetch_discussions(self,
                                    repo: Repository,
                                    numbers: list,
                                    output_folder: str,
                                    thread_num: int = 10,
                                    time_out: float = 60*60,
                                    progress_bar=None,
                                    ):
        if len(numbers) == 0:
            self._print_warn("Discussions number list is empty, skip the work")
            return
        if time_out <= 0:
            self._print_warn("Timeout value is less or equal to 0, skip the work")
            return

        start = time.time()

        repo_info = _repo_info(repo)
        repo_full_name = repo_info["full_name"]
        repo_folder, repo_file_path = construct_repo_folder(repo_full_name,
                                                            output_folder,
                                                            logger=self._logger)
        target_folder = os.path.join(repo_folder, "discussions")
        os.makedirs(name=target_folder, exist_ok=True)

        numbers_done = self._find_done_numbers(target_folder)
        numbers = list(set(numbers).difference(set(numbers_done)))
        self._print_info("{:d} numbers have been done, {:d} numbers left".format(len(numbers_done), len(numbers)))
        if len(numbers) == 0:
            self._print_warn("Discussions number list is empty, skip the work")
            return

        discussion_list = []
        threads_alive = []
        lock_list = Lock()
        self._stop_all = False

        def _worker_get_discussions(repo_full_name: str,
                                    numbers: list,
                                    ):
            thread_name = threading.current_thread().name[:T_NAME_LEN]
            for number in numbers:
                if self._stop_all:
                    break
                fet = FetchIssues("", logger=self._logger, filter=self._filter)
                info = fet.get_discussion(repo_full_name=repo_full_name, number=number)
                if info:
                    lock_list.acquire()
                    discussion_list.append(info)
                    if len(discussion_list) % 10 == 0:
                        self._print_info("[{:s}] {:d} discussions have been parsed"
                                         .format(thread_name, len(discussion_list)))
                    if len(discussion_list) >= 1000:
                        self._dump_file(target_folder, discussion_list)
                        discussion_list.clear()
                    lock_list.release()
            self._wait_continue()

        total_count = len(numbers)
        while len(numbers) > 0:
            if self._stop_all:
                break

            batch = int(len(numbers) / (2 * thread_num))
            if batch < 1:
                batch = 1

            self._call_progressbar(progress_bar,
                                   "Fetching discussions of repo '{:s}'".format(repo_full_name),
                                   total_count-len(numbers),
                                   total_count)

            batch_numbers = numbers[0:batch]
            numbers = numbers[batch:]
            t = Thread(target=_worker_get_discussions, args=(repo.full_name, batch_numbers,))
            threads_alive.append(t)
            t.start()
            self._print_info("Create new thread '{:s}' for numbers: {}".format(t.name, batch_numbers))
            if len(threads_alive) >= thread_num:
                threads_alive, threads_done = self._wait_thread(threads=threads_alive,
                                                                time_start=start,
                                                                time_out=time_out)

        self._wait_thread(threads=threads_alive,
                          time_start=start,
                          time_out=time_out,
                          wait_all=True)

        if len(discussion_list) > 0:
            self._dump_file(target_folder, discussion_list)

        self._call_progressbar(progress_bar,
                               "Fetching discussions of repo '{:s}'".format(repo_full_name),
                               total_count,
                               total_count)

        end = time.time()
        time_cost = end - start
        self._print_info("Fetch discussions for '{:s}' finished, totally fetch {:d} discussions, time cost: {:s}"
                         .format(repo_full_name, len(discussion_list), format_time_cost(time_cost)))

    # output_issues is a callback func like: def output_issue(issue_info: {})
    def _worker_fetch_issues(self,
                             token: str,
                             repo_full_name: Repository,
                             numbers: list,
                             output_issue=None,
                             ):
        start = time.time()
        thread_name = threading.current_thread().name[:T_NAME_LEN]
        try:
            msg = "Fetch issues in {:d} numbers".format(len(numbers))
            self._print_info(msg)

            desc = DescribeRepo(token, logger=self._logger)
            status, repo = desc.get_repo(repo_full_name)
            if not status.OK():
                self._print_err("[{:s}] Failed to get repo, error: {:s}"
                                .format(thread_name, status.message))
                return

            count = 0
            for number in numbers:
                if self._stop_all:
                    break

                self._print_info("[{:s}] Get issue for number {:d}"
                                 .format(thread_name, number))
                rate_limit = desc.get_rate_limit()
                _wait_rate_limit(rate_limit=rate_limit,
                                 show_me=True,
                                 core_remain_alert=50,
                                 logger=self._logger,
                                 )
                issue = repo.get_issue(number)
                if not issue:
                    continue

                issue_info = _issue_info(issue)
                count = count + 1
                if count % 10 == 0:
                    self._print_info("[{:s}] {:d} of {:d} issues have been parsed"
                                     .format(thread_name, count, len(numbers)))
                # no answers, skip
                if ("comments" not in issue_info) or len(issue_info["comments"]) == 0:
                    continue
                if output_issue:
                    output_issue(issue_info)
        except Exception as e:
            self._print_err("[{:s}] Failed to fetch issues in {:d} numbers, error: {}"
                            .format(thread_name, len(numbers), e))

        end = time.time()
        msg = "[{:s}] Fetch issues in {:d} numbers finished, time cost: {:s}"\
            .format(thread_name, len(numbers), format_time_cost(end - start))
        self._print_info(msg)
        self._wait_continue()

    def _parallel_fetch_issues(self,
                               repo: Repository,
                               numbers: list,
                               output_folder: str,
                               time_out: float = 60 * 60 * 2,
                               progress_bar=None,
                               ):
        if len(numbers) == 0:
            self._print_warn("Issues number list is empty, skip the work")
            return
        if time_out <= 0:
            self._print_warn("Timeout value is less or equal to 0, skip the work")
            return

        start = time.time()

        repo_info = _repo_info(repo)
        repo_full_name = repo_info["full_name"]
        repo_folder, repo_file_path = construct_repo_folder(repo_full_name,
                                                            output_folder,
                                                            logger=self._logger)
        target_folder = os.path.join(repo_folder, "issues")
        os.makedirs(name=target_folder, exist_ok=True)

        numbers_done = self._find_done_numbers(target_folder)
        numbers = list(set(numbers).difference(set(numbers_done)))
        self._print_info("{:d} numbers have been done, {:d} numbers left".format(len(numbers_done), len(numbers)))
        if len(numbers) == 0:
            self._print_warn("Issues number list is empty, skip the work")
            return

        issues_list = []
        lock_list = Lock()
        stat = {"count": 0}
        total_count = len(numbers)

        def receive_issue(issue_info: {}):
            lock_list.acquire()
            issues_list.append(issue_info)
            stat["count"] = stat["count"] + 1
            self._call_progressbar(progress_bar,
                                   "Fetching issues of repo '{:s}'".format(repo_full_name),
                                   stat["count"],
                                   total_count)

            if len(issues_list) >= 1000:
                self._dump_file(target_folder, issues_list)
                issues_list.clear()
            lock_list.release()

        idle_tokens = set()
        for tk in self._tokens:
            idle_tokens.add(tk)

        def done_handler(threads_done: []):
            for t in threads_done:
                self._print_info("Download thread '{:s}' done".format(t.name[:T_NAME_LEN]))
                idle_tokens.add(t.name)

        threads_alive = []
        thread_num = len(self._tokens)
        self._stop_all = False
        while len(numbers) > 0:
            if self._stop_all:
                break

            batch = int(len(numbers) / (2 * len(self._tokens)))
            if batch < 1:
                batch = 1

            batch_numbers = numbers[0:batch]
            numbers = numbers[batch:]
            token = idle_tokens.pop()
            t = Thread(target=self._worker_fetch_issues,
                       name=token,
                       args=(token, repo.full_name, batch_numbers, receive_issue,))
            threads_alive.append(t)
            t.start()
            self._print_info("Create new thread with token {:s} for {:d} numbers: {}"
                             .format(token[:T_NAME_LEN], len(batch_numbers), batch_numbers))
            if len(threads_alive) >= thread_num:
                threads_alive, threads_done = self._wait_thread(threads=threads_alive,
                                                                time_start=start,
                                                                time_out=time_out)
                done_handler(threads_done)

        self._wait_thread(threads=threads_alive,
                          time_start=start,
                          time_out=time_out,
                          wait_all=True)

        if len(issues_list) > 0:
            self._dump_file(target_folder, issues_list)

        self._call_progressbar(progress_bar,
                               "Fetching issues of repo '{:s}'".format(repo_full_name),
                               total_count,
                               total_count)

        end = time.time()
        time_cost = end - start
        self._print_info("Fetch issues for '{:s}' finished, totally fetch {:d} issues, time cost: {:s}"
                         .format(repo_full_name, stat["count"], format_time_cost(time_cost)))

    def parallel_fetch_issues_discussions(self,
                                          repo_full_name: str,
                                          output_folder: str,
                                          time_out: float = 60 * 60 * 2,
                                          progress_bar=None,
                                          fetch_issues: bool = True,
                                          fetch_discussions: bool = True,
                                          ):
        """Fetch issues by multi-threads.
            :param repo_full_name: target repo.
            :param output_folder: target folder to store files
            :param time_out: timeout value to force stop all threads, units: second.
            :param progress_bar: def show_progress(title:str, current:int, total:int).
            :param fetch_discussions: fetch issues or not
            :param fetch_issues: fetch discussions or not
            """
        if len(self._tokens) == 0:
            self._print_warn("No token provided for fetching issues")
            return
        if time_out <= 0:
            self._print_warn("Timeout value is less or equal to 0, skip the work")
            return

        start = time.time()
        desc = DescribeRepo(self._token, logger=self._logger)
        status, repo = desc.get_repo(repo_full_name)
        if not status.OK():
            self._print_err("Failed to get repo: {}".format(status.message))
            return

        number_progress_percent = 10
        issue_progress_percent = 70
        discussion_progress_percent = 20

        def get_numbers_progress(title: str, current: int, total: int):
            percent = number_progress_percent * current / total
            self._call_progressbar(progress_bar, title, int(percent), 100)

        fet = FetchIssues(token=self._tokens[0], logger=self._logger, filter=self._filter)
        status, issue_numbers, pull_numbers, discus_numbers =\
            fet._get_issue_pull_numbers(repo=repo, progress_bar=get_numbers_progress)
        msg = "Issues numbers: {:d}\t{}".format(len(issue_numbers), issue_numbers)
        self._print_info(msg)
        msg = "Pull requests numbers: {:d}\t{}".format(len(pull_numbers), pull_numbers)
        self._print_info(msg)
        msg = "Discussion numbers: {:d}\t{}".format(len(discus_numbers), discus_numbers)
        self._print_info(msg)

        if fetch_issues:
            def fetch_issues_progress(title: str, current: int, total: int):
                percent = number_progress_percent + issue_progress_percent * current / total
                if percent > 100:
                    print(current, total)
                self._call_progressbar(progress_bar, title, int(percent), 100)

            time_cost = time.time() - start
            time_left = time_out - time_cost
            start = time.time()
            self._parallel_fetch_issues(repo=repo,
                                        numbers=issue_numbers,
                                        output_folder=output_folder,
                                        time_out=time_left,
                                        progress_bar=fetch_issues_progress,
                                        )

        if fetch_discussions:
            def fetch_discussions_progress(title: str, current: int, total: int):
                percent = number_progress_percent+issue_progress_percent+discussion_progress_percent*current/total
                self._call_progressbar(progress_bar, title, int(percent), 100)

            time_cost = time.time() - start
            time_left = time_out - time_cost
            self._parallel_fetch_discussions(repo=repo,
                                             numbers=discus_numbers,
                                             output_folder=output_folder,
                                             time_out=time_left,
                                             progress_bar=fetch_discussions_progress,
                                             )

    def _find_done_numbers(self, folder: str):
        numbers_done = []
        for parent, dirnames, filenames in os.walk(folder):
            if parent is folder:
                for filename in filenames:
                    ext = os.path.splitext(filename)
                    if len(ext) != 2 or ext[1] != ".json":
                        continue
                    fullpath = os.path.join(parent, filename)

                    with open(fullpath, encoding='utf-8') as f:
                        content = json.load(f)
                        if "items" in content.keys():
                            for item in content["items"]:
                                numbers_done.append(item["number"])
                break
        return numbers_done
