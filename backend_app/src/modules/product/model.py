from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from datetime import datetime

from src.core.db.base import Base


class Product(Base):
    """
    Product database model
    """

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False, index=True)

    category = Column(String, nullable=False, index=True)

    price = Column(Float, nullable=False)

    rating = Column(Float, default=0)

    created_at = Column(DateTime, default=datetime.utcnow, index=True)

    # Soft delete flag
    is_deleted = Column(Boolean, default=False)
