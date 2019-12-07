import os
import json
import logging.config

class LoggingUtils:
    def __init__(self, path):
        with open(path, 'rt') as f:
            _config_dict = json.load(f)
            logging.config.dictConfig(_config_dict)
            logging.basicConfig()

    def get_logger(self, name):
        self.logger = logging.getLogger(name)
    
    def log_error(self, message):
        self.logger.error(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_info(self, message):
        self.logger.info(message)

    def log_debug(self, message):
        self.logger.debug(message)