import jwt
from datetime import datetime, timedelta, UTC

from config import Config


def generate_token(user):
    """
    Generate a JWT for a user.
    """

    payload = {
        "user_id": user.id,
        "username": user.username,
        "role": user.role,
        "exp": datetime.now(UTC) + timedelta(hours=24)
    }

    return jwt.encode(
        payload,
        Config.JWT_SECRET_KEY,
        algorithm="HS256"
    )


def verify_token(token):
    """
    Verify a JWT and return its payload.
    """

    return jwt.decode(
        token,
        Config.JWT_SECRET_KEY,
        algorithms=["HS256"]
    )