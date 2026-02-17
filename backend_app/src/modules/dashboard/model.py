from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class ProductSummary(BaseModel):
    """
    Lightweight product model for dashboard responses
    Used for recent products and highest priced product
    """

    id: int
    name: str
    price: float
    rating: float
    created_at: datetime

    class Config:
        from_attributes = True


class DashboardSummary(BaseModel):
    """
    Dashboard summary response model
    """

    total_products: int

    average_rating: Optional[float]

    highest_priced_product: Optional[ProductSummary]

    recent_products: List[ProductSummary]
