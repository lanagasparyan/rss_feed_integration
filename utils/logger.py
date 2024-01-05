# logger.py

import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(name, log_file, level=logging.INFO):
    """
    Sets up a logger with a rotating file handler.

    :param name: Name of the logger.
    :param log_file: Path to the log file.
    :param level: Logging level.
    :return: Logger object.
    """
    # Create a logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create a file handler that logs even debug messages
    if not os.path.exists('logs'):
        os.makedirs('logs')
    file_handler = RotatingFileHandler(log_file, maxBytes=1024*1024*5, backupCount=5)
    file_handler.setLevel(level)

    # Create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    return logger

# Example usage
rss_logger = setup_logger('rss_logger', 'logs/rss_feed_integration.log')
rss_logger.info('Logger setup complete.')
