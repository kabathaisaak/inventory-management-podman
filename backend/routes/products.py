from flask import Blueprint, jsonify, request

from validators.product_validator import validate_product
from logging_config.logger import logger

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

    page = request.args.get("page", default=1, type=int)
    limit = request.args.get("limit", default=10, type=int)
    name = request.args.get("name")
    sort = request.args.get("sort", default="id")
    order = request.args.get("order", default="asc")

    logger.info(
        f"Fetching products page={page}, "
        f"limit={limit}, "
        f"name={name}, "
        f"sort={sort}, "
        f"order={order}"
    )

    products = get_all_products(
        page,
        limit,
        name,
        sort,
        order
    )

    return jsonify(products)

@products_bp.route("/products/<int:id>", methods=["GET"])
def get_product(id):
    logger.info(f"Fetching product with ID {id}")

    product = get_product_by_id(id)

    if product is None:
        logger.warning(f"Product with ID {id} not found")

        return jsonify({
            "success": False,
            "message": "Product not found"
        }), 404

    return jsonify(product)


@products_bp.route("/products", methods=["POST"])
def create_product():

    data = request.get_json()

    error = validate_product(data)

    if error:
        logger.warning(f"Validation failed while creating product: {error}")

        return jsonify({
            "success": False,
            "message": error
        }), 400

    new_id = create_product_service(
        data["name"],
        data["price"]
    )

    logger.info(f"Product created successfully with ID {new_id}")

    return jsonify({
        "success": True,
        "message": "Product created",
        "id": new_id
    }), 201


@products_bp.route("/products/<int:id>", methods=["PUT"])
def update_product(id):

    data = request.get_json()

    error = validate_product(data)

    if error:
        logger.warning(f"Validation failed while updating product {id}: {error}")

        return jsonify({
            "success": False,
            "message": error
        }), 400

    update_product_service(
        id,
        data["name"],
        data["price"]
    )

    logger.info(f"Product {id} updated successfully")

    return jsonify({
        "success": True,
        "message": "Product updated"
    })


@products_bp.route("/products/<int:id>", methods=["DELETE"])
def delete_product(id):

    delete_product_service(id)

    logger.info(f"Product {id} deleted successfully")

    return jsonify({
        "success": True,
        "message": "Product deleted"
    })