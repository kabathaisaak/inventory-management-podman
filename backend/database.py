from contextlib import contextmanager
import psycopg2

from config import Config


@contextmanager
def get_cursor():

    conn = psycopg2.connect(
        host=Config.DB_HOST,
        database=Config.DB_NAME,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        port=Config.DB_PORT
    )

    cur = conn.cursor()

    try:
        yield cur
        conn.commit()

    except Exception:
        conn.rollback()
        raise

    finally:
        cur.close()
        conn.close()