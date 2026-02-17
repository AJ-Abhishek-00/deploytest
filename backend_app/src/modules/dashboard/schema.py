from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class ProductSummary(BaseModel):

    id: int
    name: str
    price: float
    rating: float
    created_at: datetime

    class Config:
        from_attributes = True


class DashboardSummaryResponse(BaseModel):

    total_products: int

    average_rating: Optional[float]

    highest_priced_product: Optional[ProductSummary]

    recent_products: List[ProductSummary]
