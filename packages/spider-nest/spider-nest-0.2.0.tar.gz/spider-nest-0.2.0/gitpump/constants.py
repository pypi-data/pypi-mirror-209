
# global constants
API_RETRY = 3
API_TIME_OUT = 30
TIME_ZONE = 8
T_NAME_LEN = 16

# constants for search
RESULT_PER_PAGE = 100
RESULT_LIMIT_PER_SEARCH = 1000

# constants for describe
CONTRIBUTOR_NUM = 3


class Status:
    SUCCESS = 0
    FAILED = 1
    RESULT_EXCEED_LIMIT = 10

    def __init__(self, code=SUCCESS, message="Success"):
        self.code = code
        self.message = message

    def __repr__(self):
        attr_list = [f'{key}={value}' for key, value in self.__dict__.items()]
        return f"{self.__class__.__name__}({', '.join(attr_list)})"

    def __eq__(self, other):
        """ Make Status comparable with self by code """
        if isinstance(other, int):
            return self.code == other

        return isinstance(other, self.__class__) and self.code == other.code

    def __ne__(self, other):
        return self != other

    def OK(self):
        return self.code == Status.SUCCESS
