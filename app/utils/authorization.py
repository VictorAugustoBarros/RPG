from flask import request, Response
from functools import wraps
from config.config import Config


class Authorization:

    @staticmethod
    def auth(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            request.headers.get("authorization")

            if request.headers.get("authorization") != Config().auth():
                return Response("Authorization failed!", 401)
            return f(*args, **kwargs)

        return decorated
