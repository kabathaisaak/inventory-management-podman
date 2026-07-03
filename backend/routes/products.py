from flask import Blueprint, jsonify, request
from validators.product_validator import validate_product

from services.product_service import (
    get_all_products,
    get_product_by_id,
    create_product as create_product_service,
    update_product as update_product_service,
    delete_product as delete_product_service,
)

products_bp = Blueprint("products", __name__)


@products_bp.route("/products", methods=["GET"])
def get_products():
    return jsonify(get_all_products())


@products_bp.route("/products/<int:id>", methods=["GET"])
def get_product(id):
    product = get_product_by_id(id)

    if product is None:
        return jsonify({"message": "Product not found"}), 404

    return jsonify(product)


@products_bp.route("/products", methods=["POST"])
def create_product():

    data = request.get_json()

    error = validate_product(data)

    if error:
        return jsonify({
            "success": False,
            "message": error
        }), 400

    new_id = create_product_service(
        data["name"],
        data["price"]
    )

    return jsonify({
        "success": True,
        "message": "Product created",
        "id": new_id
    }), 201



@products_bp.route("/products/<int:id>", methods=["DELETE"])
def delete_product(id):
    delete_product_service(id)

    return jsonify({
        "message": "Product deleted"
    })