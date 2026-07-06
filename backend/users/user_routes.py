from flask import Blueprint, request, g

from auth.auth_middleware import jwt_required
from auth.roles import roles_required

from logging_config.logger import logger

from utils.response import success_response

from users.user_service import (
    get_all_users,
    get_user_by_id,
    update_user_role,
    delete_user
)

users_bp = Blueprint("users", __name__)


@users_bp.route("/users", methods=["GET"])
@jwt_required
@roles_required("admin")
def users():
    logger.info("Fetching users")

    return success_response(
        get_all_users(),
        "Users retrieved successfully"
    )

# @users_bp.route("/users/<int:user_id>", methods=["GET"])
# @jwt_required
# @roles_required("admin")
# def user(user_id):

#     return success_response(
#         get_user_by_id(user_id),
#         "User retrieved successfully"
#     )

@users_bp.route("/me", methods=["GET"])
@jwt_required
def me():

    return success_response(
        g.user,
        "Current user"
    )

@users_bp.route("/users/<int:user_id>", methods=["GET"])
@jwt_required
@roles_required("admin")
def user(user_id):
    logger.info(f"Fetching user with ID: {user_id}")

    return success_response(
        get_user_by_id(user_id),
        "User retrieved successfully"
    )

@users_bp.route("/users/<int:user_id>", methods=["DELETE"])
@jwt_required
@roles_required("admin")
def remove_user(user_id):
    logger.info(f"Removing user with ID: {user_id}")

    delete_user(user_id)

    return success_response(
        None,
        "User deleted successfully"
    )

@users_bp.route("/users/<int:user_id>/role", methods=["PATCH"])
@jwt_required
@roles_required("admin")
def role(user_id):

    data = request.get_json()

    role = data.get("role")

    if role not in ["admin", "user"]:
        return {
            "success": False,
            "message": "Invalid role"
        }, 400

    return success_response(
        update_user_role(user_id, role),
        "Role updated successfully"
    )