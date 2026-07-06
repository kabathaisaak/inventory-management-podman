import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    DB_HOST = os.getenv("DB_HOST")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_PORT = os.getenv("DB_PORT")

    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_REFRESH_SECRET = os.getenv("JWT_REFRESH_SECRET")

    ACCESS_TOKEN_EXPIRES = int(
        os.getenv("ACCESS_TOKEN_EXPIRES", "15")
    )

    REFRESH_TOKEN_EXPIRES = int(
        os.getenv("REFRESH_TOKEN_EXPIRES", "7")
    )