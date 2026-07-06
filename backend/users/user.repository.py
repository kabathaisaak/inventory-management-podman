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

        return User(*row)


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

        return User(*row)


def create_user(username, password, role="user"):

    with get_cursor() as cur:

        cur.execute(
            """
            INSERT INTO users(
                username,
                password,
                role
            )
            VALUES (%s,%s,%s)
            RETURNING id
            """,
            (
                username,
                password,
                role
            )
        )

        return cur.fetchone()[0]


def find_all():

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
            ORDER BY id
            """
        )

        rows = cur.fetchall()

        return [
            User(*row).to_dict()
            for row in rows
        ]


def update_role(user_id, role):

    with get_cursor() as cur:

        cur.execute(
            """
            UPDATE users
            SET role=%s
            WHERE id=%s
            """,
            (role, user_id)
        )


def delete(user_id):

    with get_cursor() as cur:

        cur.execute(
            """
            DELETE
            FROM users
            WHERE id=%s
            """,
            (user_id,)
        )