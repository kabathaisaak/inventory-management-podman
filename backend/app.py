from flask import Flask, jsonify

from routes.products import products_bp

app = Flask(__name__)

app.register_blueprint(products_bp)


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