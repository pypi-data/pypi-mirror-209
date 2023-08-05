"""Logging utilities."""

from logging import Logger


def print_info(logger: Logger, obj):
    if logger:
        logger.info(obj)
    print(obj)


def print_warn(logger: Logger, obj):
    if logger:
        logger.warning(obj)
    print(obj)


def print_err(logger: Logger, obj):
    if logger:
        logger.error(obj)
    print(obj)
