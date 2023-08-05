import threading

from github import (
    Github,
    RateLimit,
    Repository,
    Issue,
)

from .constants import (
    TIME_ZONE,
    T_NAME_LEN,
)

from .constants import (
    API_RETRY,
    API_TIME_OUT,
    RESULT_PER_PAGE,
)

from logging import Logger
from retry import retry
from datetime import timedelta
import datetime
import time
import requests
import os


def _wait_rate_limit(rate_limit: RateLimit,
                     show_me: bool = False,
                     core_remain_alert: int = 25,
                     search_remain_alert: int = 3,
                     interval: int = 20,
                     logger: Logger = None):
    try:
        tag = threading.current_thread().name[:T_NAME_LEN]
        core_reset = rate_limit.core.reset+timedelta(hours=TIME_ZONE)
        search_reset = rate_limit.search.reset+timedelta(hours=TIME_ZONE)
        msg = "[{:s}] Core remain:{:d} reset:{:s} | Search remain:{:d} reset:{:s}"\
            .format(tag,
                    rate_limit.core.remaining,
                    core_reset.strftime('%Y-%m-%d %H:%M:%S'),
                    rate_limit.search.remaining,
                    search_reset.strftime('%Y-%m-%d %H:%M:%S'))
        if show_me:
            print(msg)
            if logger:
                logger.info(msg)
        # wait limit reset

        if rate_limit.core.remaining < core_remain_alert:
            diff = core_reset - datetime.datetime.now()
            while diff.days >= 0 and diff.seconds >= 0:
                newmsg = msg+", wait {:d} seconds to reset...".format(diff.seconds)
                print(newmsg)
                if logger:
                    logger.info(newmsg)
                time.sleep(interval)
                diff = core_reset - datetime.datetime.now()

        if rate_limit.search.remaining < search_remain_alert:
            diff = search_reset - datetime.datetime.now()
            while diff.days >= 0 and  diff.seconds >= 0:
                newmsg = msg+", wait {:d} seconds to reset...".format(diff.seconds)
                print(newmsg)
                if logger:
                    logger.info(newmsg)
                time.sleep(1)
                diff = search_reset - datetime.datetime.now()
    except Exception as e:
        print(e)
        if logger:
            logger.error(e)


def check_rate_limit(token: str,
                     core_remain_gt: int = 0,
                     logger: Logger = None):
    try:
        g = Github(login_or_token=token, retry=API_RETRY, per_page=RESULT_PER_PAGE, timeout=API_TIME_OUT)
        rate_limit = g.get_rate_limit()
        if rate_limit.core.remaining >= core_remain_gt:
            return True
    except Exception as e:
        msg = "'{:s}' is not a valid github token: {}".format(token, e)
        print(msg)
        if logger:
            logger.error(msg)
    return False


def pick_the_best_token(tokens: [],
                        core_remain_gt: int = 0,
                        logger: Logger = None) -> str:
    min_diff = 60*60*24
    min_diff_token = ""
    for token in tokens:
        try:
            g = Github(login_or_token=token, retry=API_RETRY, per_page=RESULT_PER_PAGE, timeout=API_TIME_OUT)
            rate_limit = g.get_rate_limit()
            core_reset = rate_limit.core.reset + timedelta(hours=TIME_ZONE)
            diff = core_reset - datetime.datetime.now()
            if diff.seconds < min_diff:
                min_diff = diff.seconds
                min_diff_token = token
            if rate_limit.core.remaining >= core_remain_gt:
                min_diff_token = token
                break
        except Exception as e:
            msg = "'{:s}' is not a valid github token: {}".format(token[:10], e)
            print(msg)
            if logger:
                logger.error(msg)

    if len(min_diff_token) == 0:
        msg = "None of the {:d} tokens can meet the condition".format(len(tokens))
        print(msg)
        if logger:
            logger.error(msg)

    msg = "The best token: {:s}".format(min_diff_token[:10])
    print(msg)
    if logger:
        logger.info(msg)
    return min_diff_token


def _format_dt(dt: datetime.datetime) -> str:
    if dt:
        return dt.strftime('%Y-%m-%d %H:%M:%S')
    else:
        return ""


def _repo_info(repo: Repository) -> {}:
    repo_info = {}
    # repo_info["id"] = repo.id
    # repo_info["name"] = repo.name
    repo_info["full_name"] = repo.full_name
    repo_info["html_url"] = repo.html_url
    repo_info["description"] = repo.description
    repo_info["created_at"] = _format_dt(repo.created_at)
    # repo_info["updated_at"] = _format_dt(repo.updated_at)
    # repo_info["git_url"] = repo.git_url
    repo_info["ssh_url"] = repo.ssh_url
    repo_info["clone_url"] = repo.clone_url
    repo_info["homepage"] = repo.homepage
    repo_info["stargazers_count"] = repo.stargazers_count
    # repo_info["watchers_count"] = repo.subscribers_count
    repo_info["language"] = repo.language
    # repo_info["has_issues"] = repo.has_issues
    # repo_info["has_projects"] = repo.has_projects
    # repo_info["has_downloads"] = repo.has_downloads
    repo_info["has_wiki"] = repo.has_wiki
    # repo_info["has_pages"] = repo.has_pages
    repo_info["forks_count"] = repo.forks_count
    # repo_info["open_issues_count"] = repo.open_issues_count
    repo_info["topics"] = repo.topics
    repo_info["default_branch"] = repo.default_branch
    return repo_info


def construct_repo_folder(repo_full_name: str, parent_folder: str, logger: Logger = None):
    try:
        all_repo_folder = os.path.join(parent_folder, "repos/")
        os.makedirs(name=all_repo_folder, exist_ok=True)
        this_repo_folder = os.path.join(all_repo_folder, repo_full_name.replace("/", "|"))
        summary_file_path = os.path.join(this_repo_folder, "summary.json")
        return this_repo_folder, summary_file_path
    except Exception as e:
        msg = "Failed to construct repo folder, error: {}".format(e)
        print(msg)
        if logger:
            logger.error(msg)
        return "", ""


def _user_info(user) -> {}:
    user_info = {"name": user.name,
                 # "avatar_url": user.avatar_url,
                 "company": user.company,
                 "created_at": _format_dt(user.created_at),
                 "followers": user.followers,
                 "following": user.following,
                 "email": user.email,
                 "url": user.url,
                 "location": user.location,
                 }
    return user_info


def _issue_info(issue: Issue):
    issue_info = {}
    issue_info["html_url"] = issue.html_url
    # issue_info["id"] = issue.id
    issue_info["number"] = issue.number
    issue_info["state"] = issue.state
    issue_info["title"] = issue.title
    issue_info["body"] = issue.body
    issue_info["created_at"] = _format_dt(issue.created_at)
    issue_info["closed_at"] = _format_dt(issue.closed_at)
    issue_info["user"] = issue.user.name

    # labels = issue.labels
    # label_list = []
    # for label in labels:
    #     label_list.append(label.name)
    # issue_info["labels"] = label_list
    #
    # if issue.milestone:
    #     issue_info["milestone"] = issue.milestone.title
    # else:
    #     issue_info["milestone"] = ""

    comments_list = []
    comments = issue.get_comments()
    for comment in comments:
        comment_info = {}
        # comment_info["html_url"] = comment.html_url
        comment_info["created_at"] =  _format_dt(comment.created_at)
        comment_info["user"] = comment.user.name
        comment_info["body"] = comment.body
        comments_list.append(comment_info)
    issue_info["comments"] = comments_list

    return issue_info


def _http_headers():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) '
                      'Chrome/17.0.963.56 Safari/535.11',
        'Accept'		: 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encodin'	: 'gzip,deflate,sdch',
        'Accept-Languag'	: 'en-US,en;q=0.5'
    }
    return headers


@retry(tries=3, delay=2)
def _get_http_request(url: str, logger: Logger = None, headers=None, timeout: int = 10):
    if headers is None:
        headers = _http_headers()
    msg = "Get http url: " + url
    print(msg)
    if logger:
        logger.info(msg)
    return requests.get(url, headers=headers, timeout=timeout)


def get_http_request(url: str, logger: Logger = None, headers: {} = None, timeout: int = 10):
    try:
        resp = _get_http_request(url=url, headers=headers, logger=logger, timeout=timeout)
        if resp.status_code < 200 or resp.status_code >= 300:
            msg = "Failed to get http url: {:s}, error code: {:d}".format(url, resp.status_code)
            print(msg)
            if logger:
                logger.error(msg)
            return None
        return resp
    except Exception as e:
        msg = "Failed to get http url: {:s}, error: {}".format(url, e)
        print(msg)
        if logger:
            logger.error(msg)
    return None


@retry(tries=3, delay=2)
def _download_file(url: str, target_folder: str, target_name: str = None, timeout: float = 60, logger: Logger = None):
    msg = "Download url: " + url
    print(msg)
    if logger:
        logger.info(msg)

    try:
        start = time.time()
        target_file = os.path.basename(url)
        if target_name:
            target_file = target_name
        full_path = os.path.join(target_folder, target_file)
        response = requests.get(url, headers=_http_headers(), stream=True, timeout=timeout)
        with open(full_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024*1024):
                if chunk:
                    f.write(chunk)

        end = time.time()
        msg = "Successfully download url: {:s} to {:s}, time cost:{:s}".format(url, full_path,
                                                                               format_time_cost(end - start))
        print(msg)
        if logger:
            logger.info(msg)

    except Exception as e:
        print("Failed to download url: {:s}".format(url), e)
        if logger:
            logger.error(e)


def download_file(url: str, target_folder: str, target_name: str = None, timeout: float = 60, logger: Logger = None):
    try:
        _download_file(url=url,
                       target_folder=target_folder,
                       target_name=target_name,
                       timeout=timeout,
                       logger=logger)
    except Exception as e:
        msg = "Failed to download file: {:s}, error: {}".format(url, e)
        print(msg)
        if logger:
            logger.error(msg)


def format_time_cost(seconds: float) -> str:
    SEC_PER_M = 60
    SEC_PER_H = 60 * 60
    SEC_PER_D = 60 * 60 * 24

    if seconds < 0:
        seconds = 0

    DAY = int(seconds // SEC_PER_D)
    HOUR = int((seconds - (DAY * SEC_PER_D)) // SEC_PER_H)
    MINUTE = int((seconds - (DAY * SEC_PER_D + HOUR * SEC_PER_H)) // SEC_PER_M)
    SECOND = seconds - (DAY * SEC_PER_D + HOUR * SEC_PER_H + MINUTE * SEC_PER_M)
    MSECOND = int((SECOND - int(SECOND))*1000)
    SECOND = int(SECOND)

    if DAY > 0:
        return '({}d {}h {}m {}s {}ms)'.format(DAY, HOUR, MINUTE, SECOND, MSECOND)
    if HOUR > 0:
        return '({}h {}m {}s {}ms)'.format(HOUR, MINUTE, SECOND, MSECOND)
    if MINUTE > 0:
        return '({}m {}s {}ms)'.format(MINUTE, SECOND, MSECOND)
    if SECOND > 0:
        return '({}s {}ms)'.format(SECOND, MSECOND)

    return '({}ms)'.format(MSECOND)
