from flask import Flask, jsonify
from flasgger import Swagger
from exceptions.not_found import ResourceNotFoundError
from users.user_routes import users_bp
from routes.products import products_bp
from auth.auth_routes import auth_bp
from handlers.error_handler import register_error_handlers
from handlers import validation_handler
from utils.response import error_response

app = Flask(__name__)

register_error_handlers(app)
validation_handler(app)

app.config["SWAGGER"] = {
    "title": "Inventory Management API",
    "uiversion": 3
}

@app.errorhandler(ResourceNotFoundError)
def handle_not_found(error):
    return error_response(str(error), 404)

# Register blueprints
app.register_blueprint(products_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(users_bp)

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec",
            "route": "/apispec.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/"
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