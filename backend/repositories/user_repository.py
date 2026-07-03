from database import get_cursor
from models.user import User


def find_by_username(username):

    with get_cursor() as cur:

        cur.execute(
            """
            SELECT id, username, password, role
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
        row[3]
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
            SELECT id, username, password, role
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
        row[3]
    )