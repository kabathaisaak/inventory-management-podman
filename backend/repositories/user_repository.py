from database import get_cursor
from models.user import User


def find_by_username(username):

    with get_cursor() as cur:

        cur.execute(
            """
            SELECT
                id,
                username,
                password,
                role,
                created_at
            FROM users
            WHERE username=%s
            """,
            (username,)
        )

        row = cur.fetchone()

    if row is None:
        return None

    return User(
        row[0],
        row[1],
        row[2],
        row[3],
        row[4]
    )


def save(username, password, role="user"):

    with get_cursor() as cur:

        cur.execute(
            """
            INSERT INTO users(username, password, role)
            VALUES(%s, %s, %s)
            RETURNING id
            """,
            (
                username,
                password,
                role
            )
        )

        return cur.fetchone()[0]


def find_by_id(user_id):

    with get_cursor() as cur:

        cur.execute(
            """
            SELECT
                id,
                username,
                password,
                role,
                created_at
            FROM users
            WHERE id=%s
            """,
            (user_id,)
        )

        row = cur.fetchone()

    if row is None:
        return None

    return User(
        row[0],
        row[1],
        row[2],
        row[3],
        row[4]
    ).to_dict()


def find_all():

    with get_cursor() as cur:

        cur.execute(
            """
            SELECT
                id,
                username,
                role,
                created_at
            FROM users
            ORDER BY id
            """
        )

        rows = cur.fetchall()

    return [
        {
            "id": row[0],
            "username": row[1],
            "role": row[2],
            "created_at": row[3]
        }
        for row in rows
    ]