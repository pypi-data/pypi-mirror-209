#!/usr/bin/env python
"""Jautomate entry point script."""


from jautomate import cli, __app_name__
from jautomate.logger import j_logger


def main():
    j_logger.debug("%s has started", __app_name__)
    cli.app(prog_name=__app_name__)


if __name__ == "__main__":
    main()
