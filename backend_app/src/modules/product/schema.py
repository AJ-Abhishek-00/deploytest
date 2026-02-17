from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List


class ProductCreate(BaseModel):

    name: str
    category: str
    price: float
    rating: float


class ProductResponse(BaseModel):

    id: int
    name: str
    category: str
    price: float
    rating: float
    created_at: datetime

    class Config:
        from_attributes = True


class ProductListResponse(BaseModel):

    data: List[ProductResponse]

    next_cursor: Optional[str]

    has_more: bool
