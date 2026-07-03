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