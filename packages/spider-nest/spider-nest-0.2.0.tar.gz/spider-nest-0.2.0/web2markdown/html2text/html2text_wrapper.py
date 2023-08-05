from .html2text import (
    HTML2Text,
)

from logging import Logger

class HTML2TextWrapper(HTML2Text):
    def __init__(self, out=None, baseurl='', logger: Logger = None):
        HTML2Text.__init__(self, out=out, baseurl=baseurl)

        self._ignore_list = []
        self._is_in_ignore = False
        self._logger = logger

    def _print_info(self, msg):
        print(msg)
        if self._logger:
            self._logger.info(msg)

    def ignore_tag(self, tag:str):
        self._ignore_list.append(tag)

    def ignore_tags(self, tags:[]):
        self._ignore_list.extend(tags)

    def handle_starttag(self, tag, attrs):
        if tag in self._ignore_list:
            # self._print_info("Enter ignored tag '{}'".format(tag))
            self._is_in_ignore = True

        if self._is_in_ignore:
            return

        self.handle_tag(tag, attrs, 1)

    def handle_endtag(self, tag):
        if tag in self._ignore_list:
            # self._print_info("Exit ignored tag '{}'".format(tag))
            self._is_in_ignore = False
            return

        if self._is_in_ignore:
            return

        self.handle_tag(tag, None, 0)

    def handle_data(self, data):
        if self._is_in_ignore:
            return

        HTML2Text.handle_data(self, data=data)