from marshmallow import ValidationError

from utils.response import error_response


def register_validation_handler(app):

    @app.errorhandler(ValidationError)
    def handle_validation_error(err):

        return error_response(
            err.messages,
            400
        )