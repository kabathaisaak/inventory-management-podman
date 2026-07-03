from flask import jsonify

from exceptions.not_found import ProductNotFoundError
from exceptions.validation import ValidationException
from exceptions.database import DatabaseException


def register_error_handlers(app):

    @app.errorhandler(ProductNotFoundError)
    def handle_not_found(error):

        return jsonify({
            "success": False,
            "message": error.message
        }), 404


    @app.errorhandler(ValidationException)
    def handle_validation(error):

        return jsonify({
            "success": False,
            "message": error.message
        }), 400


    @app.errorhandler(DatabaseException)
    def handle_database(error):

        return jsonify({
            "success": False,
            "message": error.message
        }), 500


    @app.errorhandler(Exception)
    def handle_exception(error):

        return jsonify({
            "success": False,
            "message": "Internal server error"
        }), 500