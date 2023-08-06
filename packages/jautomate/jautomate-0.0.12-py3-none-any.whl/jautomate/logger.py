"""
Sets up a log handlers.

Errors are logged in error.log while debugging messages are sent
to the console.
"""

import logging
import os
from dotenv import load_dotenv

load_dotenv()

J_ERROR_LOG = logging.ERROR
J_DEBUG_LOG = logging.DEBUG
J_LOG_FILE = os.getenv('J_LOGS')
J_LOG_FILE_LEVEL = os.getenv('J_LOG_FILE_LEVEL', 'ERROR')


def init_logger():
    # Set up logging, debug will output to stream, errors will log to file.
    logger = logging.getLogger("jautomate")
    logger.setLevel(J_DEBUG_LOG)

    if J_LOG_FILE:
        error_handler = logging.FileHandler(J_LOG_FILE)
        error_handler.setLevel(J_ERROR_LOG)
        error_formater = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        error_handler.setFormatter(error_formater)
        logger.addHandler(error_handler)

    debug_handler = logging.StreamHandler()
    debug_handler.setLevel(J_DEBUG_LOG)
    debug_formater = logging.Formatter(
        '%(name)s - %(levelname)s - %(message)s')
    debug_handler.setFormatter(debug_formater)

    logger.addHandler(debug_handler)

    return logger


j_logger = init_logger()
