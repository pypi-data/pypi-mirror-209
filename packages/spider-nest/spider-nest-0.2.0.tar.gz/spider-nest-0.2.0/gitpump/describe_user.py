
from .base import (
    Base,
)

from .util import (
    _wait_rate_limit,
    _user_info,
)

from logging import Logger


class DescribeUser(Base):
    def __init__(self, token: str, logger: Logger = None):
        super().__init__(token=token, logger=logger)

    def get_user_by_token(self):
        try:
            rate_limit = self._g.get_rate_limit()
            _wait_rate_limit(rate_limit=rate_limit, show_me=True, core_remain_alert=15, logger=self._logger)

            user = self._g.get_user()
            return _user_info(user)
        except Exception as e:
            self._print_err("Failed to get user by token, error: {}".format(e))
            return None
