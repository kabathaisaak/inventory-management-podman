from flask import Flask, jsonify
from flasgger import Swagger
from exceptions.not_found import ResourceNotFoundError
from handlers.validator_handler import register_validation_handler
from users.user_routes import users_bp
from routes.products import products_bp
from auth.auth_routes import auth_bp
from handlers.error_handler import register_error_handlers
from utils.response import error_response
# from handlers.duplicate_handler import register_duplicate_handler
from handlers.global_handler import register_global_handler
# from handlers.not_found_handler import register_not_found_handler

app = Flask(__name__)

register_error_handlers(app)
register_validation_handler(app)
# register_duplicate_handler(app)
register_global_handler(app)
# register

API_PREFIX = "/api/v1"

app.register_blueprint(
    products_bp,
    url_prefix=API_PREFIX
)

app.register_blueprint(
    users_bp,
    url_prefix=API_PREFIX
)

app.register_blueprint(
    auth_bp,
    url_prefix=API_PREFIX
)

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec",
            "route": "/apispec.json",
        }
    ],
}

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Inventory API",
        "version": "1.0.0"
    },
    "basePath": "/api/v1"
}

template = {
    "swagger": "2.0",
    "info": {
        "title": "Inventory Management API",
        "description": "REST API for Inventory Management",
        "version": "1.0.0"
    },
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "Enter your JWT as: Bearer <token>"
        }
    }
}

Swagger(
    app,
    config=swagger_config,
    template=template
)


@app.route("/")
def home():
    return jsonify({
        "message": "Inventory Management API",
        "status": "Running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "Healthy"
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )