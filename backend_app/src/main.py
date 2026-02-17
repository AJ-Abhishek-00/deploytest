import uvicorn

from src.app import app

from src.core.db.base import Base
from src.core.db.session import engine


# Create tables
Base.metadata.create_all(bind=engine)


if __name__ == "__main__":

    uvicorn.run(
        "src.app:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
