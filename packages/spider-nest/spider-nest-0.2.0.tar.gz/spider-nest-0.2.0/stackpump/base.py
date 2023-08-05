import threading

from .util import (
    format_time_cost,
)

from logging import Logger
import time


class Base:
    def __init__(self, logger: Logger = None):
        self._logger = logger
        self._stop_all = False
        self._evt_wait = threading.Event()

    def _wait_continue(self):
        self._evt_wait.set()

    def _print_info(self, msg):
        print(msg)
        if self._logger:
            self._logger.info(msg)

    def _print_warn(self, msg):
        print(msg)
        if self._logger:
            self._logger.warning(msg)

    def _print_err(self, msg):
        print(msg)
        if self._logger:
            self._logger.error(msg)

    def _wait_thread(self, threads: [],
                     time_start: float,
                     time_out: float,
                     interval: int = 3,
                     wait_all: bool = False):
        if len(threads) == 0:
            return [], []
        while True:
            alive_threads = []
            done_threads = []
            for t in threads:
                if t.is_alive():
                    alive_threads.append(t)
                else:
                    done_threads.append(t)
            self._evt_wait.clear()
            self._print_info("{:d} of {:d} threads alive".format(len(alive_threads), len(threads)))
            if ((time.time() - time_start) > time_out) and (not self._stop_all):
                self._print_warn("Time exceeds {:s}, stop all threads".format(format_time_cost(time_out)))
                self._stop_all = True
            if wait_all:
                if len(alive_threads) == 0:
                    return [], done_threads
            elif len(alive_threads) < len(threads):
                return alive_threads, done_threads
            self._evt_wait.wait(timeout=interval)

    def _call_progressbar(self, progress_bar, title: str, current: int, total: int):
        if progress_bar:
            try:
                progress_bar(title, current, total)
            except Exception as e:
                self._print_err("Failed to call progress bar, error: {}".format(e))

