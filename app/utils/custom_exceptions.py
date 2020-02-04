# -*- coding: utf-8 -*-
import traceback
import random
import string
from utils.logger import Logger
from utils.database import Database


class ExceptionHandler:

    @staticmethod
    def handler(exception):

        try:
            # Database('sms').rollback()
            return {"error": exception.args[0]["msg"]}, exception.args[0]["code"]

        except Exception as e:
            code = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
            Logger().error(traceback.format_exc())
            return {"error": "Internal server error! "
                    "For more information, please, send us this code: [%s]" % code}, 500


class NoRangeLimitException(Exception):
    pass


class InvalidDateFormatException(Exception):
    pass


class InvalidCompanyIdException(Exception):
    pass
