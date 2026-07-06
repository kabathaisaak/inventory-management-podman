from functools import wraps

from flask import g

from utils.response import error_response


def roles_required(*roles):

    def decorator(f):

        @wraps(f)
        def wrapper(*args, **kwargs):

            user = getattr(g, "user", None)

            if user is None:
                return error_response(
                    "Unauthorized",
                    401
                )

            if user["role"] not in roles:
                return error_response(
                    "Forbidden",
                    403
                )

            return f(*args, **kwargs)

        return wrapper

    return decorator