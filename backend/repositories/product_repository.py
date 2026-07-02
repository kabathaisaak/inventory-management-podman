from database import get_connection
from models.product import Product


def find_all():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT id, name, price FROM products ORDER BY id"
    )

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [
        Product(row[0], row[1], row[2]).to_dict()
        for row in rows
    ]


def find_by_id(product_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT id, name, price FROM products WHERE id=%s",
        (product_id,)
    )

    row = cur.fetchone()

    cur.close()
    conn.close()

    if row is None:
        return None

    return Product(
        row[0],
        row[1],
        row[2]
    ).to_dict()


def save(name, price):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO products(name, price)
        VALUES(%s, %s)
        RETURNING id
        """,
        (name, price)
    )

    new_id = cur.fetchone()[0]

    conn.commit()

    cur.close()
    conn.close()

    return new_id


def update(product_id, name, price):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE products
        SET name=%s,
            price=%s
        WHERE id=%s
        """,
        (name, price, product_id)
    )

    conn.commit()

    cur.close()
    conn.close()


def delete(product_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM products WHERE id=%s",
        (product_id,)
    )

    conn.commit()

    cur.close()
    conn.close()