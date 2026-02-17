from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.settings import settings

# Create database engine
engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False}  # Required for SQLite
)

# Create session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def get_db():
    """
    Dependency injection for database session
    Used in FastAPI routes
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
