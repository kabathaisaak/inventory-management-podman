from auth.auth_repository import (
    find_by_username,
    create_user
)

from auth.password import (
    hash_password,
    verify_password
)

from auth.jwt_handler import generate_token


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

    token = generate_token(user)

    return {
        "token": token,
        "user": {
            "id": user.id,
            "username": user.username,
            "role": user.role
        }
    }
