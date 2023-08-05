import threading

from logging import Logger
from retry import retry
from my_fake_useragent import UserAgent

import datetime
import time
import requests
import os


def _http_headers():
    ua = UserAgent(family='chrome')
    agent = ua.random()
    headers = {
        'User-Agent': agent,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encodin': 'gzip,deflate,sdch',
        'Accept-Languag': 'en-US,en;q=0.5'
    }
    return headers


@retry(tries=3, delay=2)
def _get_http_request(url: str, logger: Logger = None, proxy: {} = None):
    msg = "Get http url: " + url
    print(msg)
    if logger:
        logger.info(msg)
    return requests.get(url, headers=_http_headers(), timeout=10, proxies=proxy)


def get_http_request(url: str, logger: Logger = None, proxy: {} = None):
    try:
        resp = _get_http_request(url=url, logger=logger, proxy=proxy)
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
