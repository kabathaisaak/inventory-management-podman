from flask import Flask, jsonify
from flasgger import Swagger

from routes.products import products_bp
from handlers.error_handler import register_error_handlers

app = Flask(__name__)
register_error_handlers(app)

app.config["SWAGGER"] = {
    "title": "Inventory Management API",
    "uiversion": 3
}

Swagger(app)

app.register_blueprint(products_bp)

register_error_handlers(app)


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
    app.run(host="0.0.0.0", port=5000, debug=True)