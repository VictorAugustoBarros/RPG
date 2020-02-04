import copy
from flask import request
from functools import wraps
from utils.logger import Logger


class RequestLog:

    @staticmethod
    def register(f):
        @wraps(f)
        def log(*args, **kwargs):

            msg = copy.deepcopy(request.json)
            Logger().info({"body": msg, "url": request.url})

            return f(*args, **kwargs)

        return log
