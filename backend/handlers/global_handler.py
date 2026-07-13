import traceback

from logging_config.logger import logger
from utils.response import error_response


def register_global_handler(app):

    @app.errorhandler(Exception)
    def handle_exception(err):

        logger.error(traceback.format_exc())

        return error_response(
            "Internal server error",
            500
        )