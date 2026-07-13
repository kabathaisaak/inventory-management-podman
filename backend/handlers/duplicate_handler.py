from exceptions.duplicate import DuplicateUserError
from utils.response import error_response


def register_duplicate_handler(app):

    @app.errorhandler(DuplicateUserError)
    def handle_duplicate(err):

        return error_response(
            str(err),
            409
        ) 