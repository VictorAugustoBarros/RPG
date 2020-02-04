# -*- coding: utf-8 -*-i

import sys
import json
import logging
import datetime


class Logger:

    __monostate = None

    def __init__(self, name="quick-rules-api"):
        if not Logger.__monostate:

            log_format = ('{ "log_level": %(levelno)s, '
                          '"project_name": "' + name + '", '
                          '"message": %(message)s }')

            Logger.__monostate = self.__dict__
            self.logger = logging.getLogger(name)
            hdlr = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter(log_format)
            hdlr.setFormatter(formatter)
            self.logger.addHandler(hdlr)
            self.logger.setLevel(logging.DEBUG)

        else:
            self.__dict__ = Logger.__monostate

    def __default(self, o):
        if type(o) is datetime.date or type(o) is datetime.datetime:
            return o.isoformat()

    def info(self, message, **kwargs):
        message_json = json.dumps(message, ensure_ascii=False, sort_keys=True, default=self.__default)
        self.logger.info(message_json, **kwargs)

    def success(self, message, **kwargs):
        message_json = json.dumps(message, ensure_ascii=False, sort_keys=True, default=self.__default)
        self.logger.info(message_json, **kwargs)

    def error(self, message, **kwargs):
        message_json = json.dumps(message, ensure_ascii=False, sort_keys=True, default=self.__default)
        self.logger.error(message_json, **kwargs)

    def critical(self, message, **kwargs):
        message_json = json.dumps(message, ensure_ascii=False, sort_keys=True, default=self.__default)
        self.logger.critical(message_json, **kwargs)

    def debug(self, message, **kwargs):
        message_json = json.dumps(message, ensure_ascii=False, sort_keys=True, default=self.__default)
        self.logger.debug(message_json, **kwargs)
