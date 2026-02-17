from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from src.modules.product.schema import (
    ProductCreate,
    ProductResponse,
    ProductListResponse
)

from src.modules.product.service import (
    create_product,
    get_products,
    get_product_by_id,
    update_product,
    delete_product
)

from src.core.db.session import get_db


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post("", response_model=ProductResponse)
def create(
    request: ProductCreate,
    db: Session = Depends(get_db)
):

    return create_product(db, request)


@router.get("", response_model=ProductListResponse)
def list_products(
    limit: int = Query(5),
    cursor: str = None,
    search: str = None,
    category: str = None,
    min_price: float = None,
    max_price: float = None,
    sort_by: str = "created_at",
    sort_order: str = "desc",
    db: Session = Depends(get_db)
):

    return get_products(
        db,
        limit,
        cursor,
        search,
        category,
        min_price,
        max_price,
        sort_by,
        sort_order
    )


@router.get("/{product_id}", response_model=ProductResponse)
def get_by_id(
    product_id: int,
    db: Session = Depends(get_db)
):

    return get_product_by_id(
        db,
        product_id
    )


@router.put("/{product_id}", response_model=ProductResponse)
def update(
    product_id: int,
    request: ProductCreate,
    db: Session = Depends(get_db)
):

    return update_product(
        db,
        product_id,
        request
    )


@router.delete("/{product_id}")
def delete(
    product_id: int,
    db: Session = Depends(get_db)
):

    delete_product(
        db,
        product_id
    )

    return {"message": "Product deleted"}
