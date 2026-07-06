from config import Config
from users.user_repository import (
    find_by_username,
    create_user,
    find_by_id
)   

from auth.jwt_handler import (
    generate_access_token,
    generate_refresh_token,
    verify_refresh_token
)

from auth.password import (
    hash_password,
    verify_password
)


def register_user(username, password):

    existing_user = find_by_username(username)

    if existing_user:
        raise ValueError("Username already exists")

    hashed_password = hash_password(password)

    user_id = create_user(
        username,
        hashed_password
    )

    return {
        "id": user_id,
        "username": username
    }


def login_user(username, password):

    user = find_by_username(username)

    if user is None:
        raise ValueError("Invalid username or password")

    if not verify_password(password, user.password):
        raise ValueError("Invalid username or password")

    access_token = generate_access_token(user)
    refresh_token = generate_refresh_token(user)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "Bearer",
        "expires_in": Config.ACCESS_TOKEN_EXPIRES * 60,
        "user": {
            "id": user.id,
            "username": user.username,
            "role": user.role
        }
    }

def refresh_access_token(refresh_token):

    try:
        payload = verify_refresh_token(
            refresh_token
        )

    except Exception:
        raise ValueError(
            "Invalid refresh token"
        )

    user = find_by_id(
        payload["user_id"]
    )

    if user is None:
        raise ValueError(
            "User not found"
        )

    access_token = generate_access_token(
        user
    )

    return {
        "access_token": access_token,
        "token_type": "Bearer",
        "expires_in": Config.ACCESS_TOKEN_EXPIRES * 60
    }