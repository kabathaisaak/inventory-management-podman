from flask import Blueprint, request
from flasgger import swag_from
from auth.auth_middleware import jwt_required
from validators.product_validator import validate_product
from logging_config.logger import logger
from utils.response import success_response

from docs.product_docs import (
    GET_PRODUCTS_DOC,
    GET_PRODUCT_DOC,
    CREATE_PRODUCT_DOC,
    UPDATE_PRODUCT_DOC,
    DELETE_PRODUCT_DOC,
)

from services.product_service import (
    get_all_products,
    get_product_by_id,
    create_product as create_product_service,
    update_product as update_product_service,
    delete_product as delete_product_service,
)

products_bp = Blueprint("products", __name__)


@products_bp.route("/products", methods=["GET"])
@swag_from(GET_PRODUCTS_DOC)
def get_products():

    page = request.args.get("page", 1, type=int)
    limit = request.args.get("limit", 10, type=int)
    name = request.args.get("name")
    sort = request.args.get("sort", "id")
    order = request.args.get("order", "asc")

    logger.info(
        f"Fetching products page={page}, limit={limit}"
    )

    products = get_all_products(
        page,
        limit,
        name,
        sort,
        order
    )

    return success_response(products)


@products_bp.route("/products/<int:id>", methods=["GET"])
@swag_from(GET_PRODUCT_DOC)
def get_product(id):

    logger.info(f"Fetching product {id}")

    product = get_product_by_id(id)

    return success_response(product)


@products_bp.route("/products", methods=["POST"])
@jwt_required
@swag_from(CREATE_PRODUCT_DOC)
def create_product():

    data = request.get_json()

    validate_product(data)

    new_id = create_product_service(
        data["name"],
        data["price"]
    )

    logger.info(f"Created product {new_id}")

    return success_response(
        {
            "id": new_id
        },
        "Product created",
        201
    )


@products_bp.route("/products/<int:id>", methods=["PUT"])
@jwt_required
@swag_from(UPDATE_PRODUCT_DOC)
def update_product(id):

    data = request.get_json()

    validate_product(data)

    update_product_service(
        id,
        data["name"],
        data["price"]
    )

    logger.info(f"Updated product {id}")

    return success_response(
        None,
        "Product updated"
    )


@products_bp.route("/products/<int:id>", methods=["DELETE"])
@jwt_required
@swag_from(DELETE_PRODUCT_DOC)
def delete_product(id):

    delete_product_service(id)

    logger.info(f"Deleted product {id}")

    return success_response(
        None,
        "Product deleted"
    )