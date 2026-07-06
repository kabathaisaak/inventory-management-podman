from functools import wraps

from flask import request, g

from auth.jwt_handler import verify_access_token


def jwt_required(f):

    @wraps(f)
    def decorated(*args, **kwargs):

        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return {
                "success": False,
                "message": "Authorization header is missing"
            }, 401

        if not auth_header.startswith("Bearer "):
            return {
                "success": False,
                "message": "Invalid authorization header"
            }, 401

        token = auth_header.split(" ")[1]

        try:

            payload = verify_access_token(token)

            g.user = payload

        except Exception:

            return {
                "success": False,
                "message": "Invalid or expired access token"
            }, 401

        return f(*args, **kwargs)

    return decorated