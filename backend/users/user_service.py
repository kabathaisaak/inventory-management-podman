from users import user_repository

from exceptions.not_found import ResourceNotFoundError


def get_all_users():

    return user_repository.find_all()


def get_user_by_id(user_id):

    user = user_repository.find_by_id(user_id)

    if user is None:
        raise ResourceNotFoundError(
            "User",
            user_id
        )

    return user.to_dict()


def update_user_role(user_id, role):

    user = user_repository.find_by_id(user_id)

    if user is None:
        raise ResourceNotFoundError(
            "User",
            user_id
        )

    user_repository.update_role(
        user_id,
        role
    )

    return {
        "id": user_id,
        "role": role
    }


def delete_user(user_id):

    user = user_repository.find_by_id(user_id)

    if user is None:
        raise ResourceNotFoundError(
            "User",
            user_id
        )

    user_repository.delete(user_id)