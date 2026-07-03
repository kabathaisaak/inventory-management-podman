from database import get_cursor
from models.product import Product


def find_all(page=1, limit=10, name=None, sort="id", order="asc"):

    offset = (page - 1) * limit

    query = """
        SELECT id, name, price
        FROM products
    """

    params = []

    if name:
        query += " WHERE LOWER(name) LIKE LOWER(%s)"
        params.append(f"%{name}%")

    query += f" ORDER BY {sort} {order.upper()}"
    query += " LIMIT %s OFFSET %s"

    params.extend([limit, offset])

    with get_cursor() as cur:
        cur.execute(query, params)
        rows = cur.fetchall()

    return [
        Product(
            row[0],
            row[1],
            row[2]
        ).to_dict()
        for row in rows
    ]


def count(name=None):

    query = "SELECT COUNT(*) FROM products"
    params = []

    if name:
        query += " WHERE LOWER(name) LIKE LOWER(%s)"
        params.append(f"%{name}%")

    with get_cursor() as cur:
        cur.execute(query, params)
        total = cur.fetchone()[0]

    return total


def find_by_id(product_id):

    with get_cursor() as cur:
        cur.execute(
            """
            SELECT id, name, price
            FROM products
            WHERE id=%s
            """,
            (product_id,)
        )

        row = cur.fetchone()

    if row is None:
        return None

    return Product(
        row[0],
        row[1],
        row[2]
    ).to_dict()


def save(name, price):

    with get_cursor() as cur:
        cur.execute(
            """
            INSERT INTO products(name, price)
            VALUES(%s, %s)
            RETURNING id
            """,
            (name, price)
        )

        new_id = cur.fetchone()[0]

    return new_id


def update(product_id, name, price):

    with get_cursor() as cur:
        cur.execute(
            """
            UPDATE products
            SET name=%s,
                price=%s
            WHERE id=%s
            """,
            (name, price, product_id)
        )


def delete(product_id):

    with get_cursor() as cur:
        cur.execute(
            """
            DELETE FROM products
            WHERE id=%s
            """,
            (product_id,)
        )