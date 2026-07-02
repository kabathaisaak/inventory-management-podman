from flask import Flask, jsonify, request

from services.product_service import (
    get_all_products,
    get_product_by_id,
    create_product as create_product_service,
    update_product as update_product_service,
    delete_product as delete_product_service,
)

app = Flask(__name__)


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


@app.route("/products", methods=["GET"])
def get_products():
    products = get_all_products()
    return jsonify(products)


@app.route("/products/<int:id>", methods=["GET"])
def get_product(id):
    product = get_product_by_id(id)

    if product is None:
        return jsonify({"message": "Product not found"}), 404

    return jsonify(product)


@app.route("/products", methods=["POST"])
def create_product():
    data = request.get_json()

    new_id = create_product_service(
        data["name"],
        data["price"]
    )

    return jsonify({
        "message": "Product created",
        "id": new_id
    }), 201


@app.route("/products/<int:id>", methods=["PUT"])
def update_product(id):
    data = request.get_json()

    update_product_service(
        id,
        data["name"],
        data["price"]
    )

    return jsonify({
        "message": "Product updated"
    })


@app.route("/products/<int:id>", methods=["DELETE"])
def delete_product(id):
    delete_product_service(id)

    return jsonify({
        "message": "Product deleted"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)