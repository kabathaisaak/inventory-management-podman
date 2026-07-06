import jwt

from datetime import datetime, timedelta, UTC

from config import Config


def generate_access_token(user):
    """
    Generate a short-lived access token.
    """

    payload = {
        "user_id": user.id,
        "username": user.username,
        "role": user.role,
        "exp": datetime.now(UTC)
        + timedelta(minutes=Config.ACCESS_TOKEN_EXPIRES)
    }

    return jwt.encode(
        payload,
        Config.JWT_SECRET_KEY,
        algorithm="HS256"
    )


def generate_refresh_token(user):
    """
    Generate a long-lived refresh token.
    """

    payload = {
        "user_id": user.id,
        "exp": datetime.now(UTC)
        + timedelta(days=Config.REFRESH_TOKEN_EXPIRES)
    }

    return jwt.encode(
        payload,
        Config.JWT_REFRESH_SECRET,
        algorithm="HS256"
    )


def verify_access_token(token):
    """
    Verify an access token.
    """

    return jwt.decode(
        token,
        Config.JWT_SECRET_KEY,
        algorithms=["HS256"]
    )


def verify_refresh_token(token):
    """
    Verify a refresh token.
    """

    return jwt.decode(
        token,
        Config.JWT_REFRESH_SECRET,
        algorithms=["HS256"]
    )