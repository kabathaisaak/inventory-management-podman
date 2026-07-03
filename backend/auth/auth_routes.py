from flask import Blueprint, request

from logging_config.logger import logger
from utils.response import success_response, error_response

from auth.auth_service import (
    register_user,
    login_user
)

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return error_response(
            "Username and password are required",
            400
        )

    try:

        user = register_user(
            username,
            password
        )

        logger.info(f"User {username} registered")

        return success_response(
            user,
            "User registered",
            201
        )

    except ValueError as error:

        logger.warning(str(error))

        return error_response(
            str(error),
            400
        )


@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return error_response(
            "Username and password are required",
            400
        )

    try:

        result = login_user(
            username,
            password
        )

        logger.info(f"User {username} logged in")

        return success_response(
            result,
            "Login successful"
        )

    except ValueError as error:

        logger.warning(str(error))

        return error_response(
            str(error),
            401
        )