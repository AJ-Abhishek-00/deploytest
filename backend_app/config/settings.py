import os
from dotenv import load_dotenv
from pathlib import Path

# Load .env file
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")


class Settings:
    """
    Centralized settings object.
    All configuration must come from here.
    """

    APP_NAME: str = os.getenv("APP_NAME", "Backend App")

    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")

    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)
    )

    REFRESH_TOKEN_EXPIRE_MINUTES: int = int(
        os.getenv("REFRESH_TOKEN_EXPIRE_MINUTES", 1440)
    )

    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "sqlite:///./data/database.db"
    )

    DEFAULT_PAGE_SIZE: int = int(
        os.getenv("DEFAULT_PAGE_SIZE", 5)
    )

    MAX_PAGE_SIZE: int = int(
        os.getenv("MAX_PAGE_SIZE", 50)
    )


settings = Settings()
