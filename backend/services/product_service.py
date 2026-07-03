import math
from repositories import product_repository


def get_all_products(
    page=1,
    limit=10,
    name=None,
    sort="id",
    order="asc"
):
    products = product_repository.find_all(
        page,
        limit,
        name,
        sort,
        order
    )

    total = product_repository.count(name)

    return {
        "page": page,
        "limit": limit,
        "total": total,
        "total_pages": math.ceil(total / limit) if limit else 0,
        "data": products
    }


def get_product_by_id(product_id):
    return product_repository.find_by_id(product_id)


def create_product(name, price):
    return product_repository.save(name, price)


def update_product(product_id, name, price):
    product_repository.update(
        product_id,
        name,
        price
    )


def delete_product(product_id):
    product_repository.delete(product_id)