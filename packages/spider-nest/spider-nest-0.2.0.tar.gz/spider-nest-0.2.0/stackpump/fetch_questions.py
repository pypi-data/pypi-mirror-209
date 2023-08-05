import time
import os
import json
import urllib.parse

from datetime import datetime, timedelta
from pyquery import PyQuery
from logging import Logger
from threading import Thread, Lock

from .base import (
    Base,
)

from .util import (
    get_http_request,
    format_time_cost,
)

from web2markdown import (
    HTML2TextWrapper,
)


class StackFilter:
    def __init__(self,
                 from_date: datetime = None,
                 votes_ge: int = 0,
                 answer_ge: int = 1,
                 require_best_answer: bool = False):
        self.from_date = from_date
        self.votes_ge = votes_ge
        self.answer_ge = answer_ge
        self.require_best_answer = require_best_answer


class FetchStackQuestions(Base):
    # proxies is a list of
    # {
    #     'http': 'http://xx.xx.xx.xx:xxxx',
    #     'https': 'https://xx.xx.xx.xx:xxxx',
    # }
    def __init__(self, logger: Logger = None, proxies: list = None):
        super().__init__(logger=logger)
        self._found_count = 0
        self._dump_count = 0
        self._parsed_count = 0
        self._reset()
        self._proxies = proxies

    def _reset(self):
        self._stop_all = False
        self._stop_parse_list = False
        self._qurstions = []
        self._found_count = 0
        self._dump_count = 0
        self._parsed_count = 0
        self._lock_q = Lock()

    def _exist_questions(self, output_folder: str) -> set:
        id_list = []
        for parent, dirnames, filenames in os.walk(output_folder):
            if parent is output_folder:
                for filename in filenames:
                    ext = os.path.splitext(filename)
                    if len(ext) != 2 or ext[1] != ".json":
                        continue
                    fullpath = os.path.join(parent, filename)

                    with open(fullpath, encoding='utf-8') as f:
                        content = json.load(f)
                        if "questions" in content.keys():
                            questions = content["questions"]
                            print("Exist questions count:", len(questions))
                            for q in questions:
                                id_list.append(q["id"])
                break

        self._print_info("{:d} questions already exist".format(len(id_list)))
        return set(id_list)

    def _output_quetions(self, question: {}, output_folder: str, force_dump: bool = False):
        self._lock_q.acquire()
        if question:
            self._qurstions.append(question)
        count = len(self._qurstions)
        dump_content = {
            "question_count": count,
        }
        if count >= 1000 or (force_dump and count > 0):
            dump_content["questions"] = self._qurstions.copy()
            self._qurstions.clear()
        self._lock_q.release()
        if "questions" in dump_content:
            q_list = dump_content["questions"]
            file_name = "questions_{}_to_{}.json".format(q_list[0]["id"], q_list[count-1]["id"])
            full_name = os.path.join(output_folder, file_name)
            try:
                with open(full_name, 'w', encoding='utf-8') as f:
                    json.dump(obj=dump_content, fp=f, indent=2, ensure_ascii=False)
                msg = "Dump file:{:s} for {:d} questions".format(full_name, count)
                self._dump_count = self._dump_count + count
                self._print_info(msg)
            except Exception as e:
                msg = "Failed to dump:{:s}, err: {}".format(full_name, e)
                self._print_err(msg)

    def parse_question(self, url: str):
        proxy = self._proxies[0] if self._proxies and (len(self._proxies) > 0) else None
        resp = get_http_request(url, logger=self._logger, proxy=proxy)
        if resp is None:
            self._print_err("Failed to open url: {:s}".format(url))
            return {}

        def __to_markdown(htm):
            h2t = HTML2TextWrapper()
            return h2t.handle(htm)

        def __content_block(pq: PyQuery) -> {}:
            try:
                text_body = PyQuery(pq)('div.js-post-body')
                md = __to_markdown(text_body.html())

                comments = PyQuery(pq)('div.comment-body')
                comment_list = []
                for cm in comments:
                    c_md = __to_markdown(PyQuery(cm).html())
                    comment_list.append(c_md)

                created_time = PyQuery(pq)('div.user-action-time span').attr('title')
                user_detail = PyQuery(pq)('div.user-details a').text()
                return {
                    "body": md,
                    "comments": comment_list,
                    "created_time": created_time,
                    "author": user_detail,
                }
            except Exception as e:
                self._print_err("Failed to parse content block, error: {}".format(e))
                return {}

        question_info = {}
        content = PyQuery(resp.content)
        header = content('div#question-header')
        question_info['title'] = PyQuery(header).text().rstrip('\nAsk Question')

        question = content('div.question')
        question_info['question'] = __content_block(question)

        answers = content('div.answer')
        answers_list = []
        for aw in answers:
            answer_info = __content_block(aw)
            best = PyQuery(aw)('div.js-accepted-answer-indicator')
            best_answer = False
            if best and (not PyQuery(best).has_class('d-none')):
                best_answer = True
            answer_info["best_answer"] = best_answer
            answers_list.append(answer_info)

        question_info["answers"] = answers_list

        self._print_info("Finish parsing {:s}".format(url))
        return question_info

    def __parse_timestr(self, t_str: str) -> datetime:
        try:
            return datetime.strptime(t_str, '%Y-%m-%d %H:%M:%SZ')
        except Exception as e:
            self._print_err("Failed to parse time, error: {}".format(e))

        return None

    def parse_questions_list(self,
                             url: str,
                             filter: StackFilter = None,
                             get_pagination: bool = False):
        proxy = self._proxies[0] if self._proxies and (len(self._proxies) > 0) else None
        resp = get_http_request(url, logger=self._logger, proxy=proxy)
        if resp is None:
            self._print_err("Failed to open url: {:s}".format(url))
            return [], 1,

        questions_base_info = []
        content = PyQuery(resp.content)
        summary_list = content('div#questions')('div.s-post-summary')
        for summary in summary_list:
            if self._stop_all:
                break

            base_info = {}
            # time
            ts = PyQuery(summary)('time span').attr('title')
            if ts is None:
                continue
            dt = self.__parse_timestr(ts)
            base_info["time"] = ts

            # votes, answers, views
            stats = PyQuery(summary)('div.s-post-summary--stats-item')
            for stat in stats:
                try:
                    num = PyQuery(stat)('span.s-post-summary--stats-item-number').text()
                    unit = PyQuery(stat)('span.s-post-summary--stats-item-unit').text()
                    if unit.startswith("vote"):
                        unit = "votes"
                    elif unit.startswith("answer"):
                        unit = "answers_count"
                        base_info["has_best_answer"] = PyQuery(stat).has_class('has-accepted-answer')
                    elif unit.startswith("view"):
                        unit = "views"
                    base_info[unit] = num if unit == "views" else int(num)
                except Exception as e:
                    self._print_err("Failed to get question's stats, error: {}".format(e))

            # id and url
            title = PyQuery(summary)('h3.s-post-summary--content-title')
            alink = PyQuery(title)('a')
            link = PyQuery(alink).attr('href')
            url = urllib.parse.urljoin('https://stackoverflow.com/', link)
            base_info["url"] = url
            base_info["id"] = link.split('/')[2]

            # filtering
            if filter:
                # require has best answer
                if filter.require_best_answer and ("has_best_answer" in base_info) and\
                        (base_info["has_best_answer"] is False):
                    continue

                if filter.from_date:
                    # arranged by datetime, stop searching if this date is older than filter.from_date
                    if dt < filter.from_date:
                        self._stop_all = True
                        return questions_base_info, 0
                    # skip items whose votes is less than filter.votes_ge
                    if filter and "votes" in base_info.keys() and int(base_info["votes"]) < filter.votes_ge:
                        continue
                else:
                    # arranged by votes, stop searching if this votes is less than filter.votes_ge
                    if base_info["votes"] < filter.votes_ge:
                        self._stop_all = True
                        return questions_base_info, 0

                # skip items whose date is older than filter.from_date
                if ("answers_count" in base_info.keys()) and (int(base_info["answers_count"]) < filter.answer_ge):
                    continue

            questions_base_info.append(base_info)

        # get pagination count
        last_page = 1
        if get_pagination:
            try:
                pagination = content('div.s-pagination')
                items = pagination('a')
                if len(items) > 1:
                    pp = PyQuery(items[len(items) - 2])
                    last_page = int(pp.text())
            except Exception as e:
                self._print_err("Failed to get pagination of: {:s}".format(url))

        self._print_info("Found {:d} questions".format(len(questions_base_info)))
        return questions_base_info, last_page

    def fetch_questions(self,
                        tag: str,
                        output_folder: str,
                        filter: StackFilter = StackFilter(),
                        time_out: float = 60*60*24,
                        progress_bar=None,
                        ):
        """Fetch trending by multi-threads.
               :param tag: tag to search questions
               :param filter: filter the questions by conditions
               :param output_folder: target folder to store files
               :param time_out: timeout value to force stop all threads, units: second.
               :param progress_bar: def show_progress(title:str, current:int, total:int).
               """
        self._print_info("Prepare to fetch question with tag {:s}".format(tag))
        start = time.time()

        self._reset()
        exist_ids = self._exist_questions(output_folder)

        def __parse_questions(base_list: []):
            for base_info in base_list:
                details = self.parse_question(base_info["url"])
                details.update(base_info)
                self._output_quetions(details, output_folder, False)
                time.sleep(2)
            self._parsed_count = self._parsed_count + len(base_list)

        if filter and filter.from_date:
            tag_url = "https://stackoverflow.com/questions/tagged/{:s}?sort=Newest".format(tag)
        else:
            tag_url = "https://stackoverflow.com/questions/tagged/{:s}?tab=votes".format(tag)

        last_page = 1
        i = 1
        threads_alive = []
        while i <= last_page:
            if self._stop_all:
                break

            # parse questions list
            url = tag_url + "&page={:d}&pagesize=50".format(i)
            get_pagination = (i == 1)
            found_list, page_count = self.parse_questions_list(url, filter, get_pagination=get_pagination)
            i = i + 1
            if get_pagination:
                last_page = page_count

            # remove question which has been parsed before
            base_list = []
            for f in found_list:
                if f["id"] not in exist_ids:
                    base_list.append(f)
            if len(base_list) == 0:
                self._print_info("All the found questions are already exist")
                continue

            self._found_count = self._found_count + len(base_list)

            # parse questions
            t = Thread(target=__parse_questions, args=(base_list,))
            threads_alive.append(t)
            t.start()
            self._print_info("Create new thread '{:s}' for parsing {:d} questions"
                             .format(t.name, len(base_list)))
            self._call_progressbar(progress_bar,
                                   "Fetching questions for {}".format(tag),
                                   self._parsed_count,
                                   self._found_count)

            # multiple threads could exceed rate limit
            if len(threads_alive) >= 1:
                threads_alive, threads_done = self._wait_thread(threads=threads_alive,
                                                                time_start=start,
                                                                time_out=time_out)

        self._wait_thread(threads=threads_alive,
                          time_start=start,
                          time_out=time_out,
                          wait_all=True)
        self._output_quetions(None, output_folder, True)
        self._call_progressbar(progress_bar,
                               "Fetching questions for {}".format(tag),
                               self._parsed_count,
                               self._found_count)

        end = time.time()
        self._print_info("Finish to fetch {:d} questions with tag {:s}, time cost: {:s}"
                         .format(self._dump_count, tag, format_time_cost(end - start)))
