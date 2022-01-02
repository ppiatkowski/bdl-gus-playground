#!/usr/bin/python3

import coloredlogs
import logging


logger = logging.getLogger(__name__)
coloredlogs.install(level="DEBUG", fmt="%(asctime)s %(levelname)s %(message)s", logger=logger)
