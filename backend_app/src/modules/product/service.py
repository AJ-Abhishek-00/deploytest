from sqlalchemy.orm import Session

from src.modules.product import crud
from src.modules.product.schema import ProductCreate
from src.utils.pagination import encode_cursor


# REQUIRED FUNCTION (YOU ARE MISSING THIS)
def create_product(
    db: Session,
    request: ProductCreate
):

    return crud.create_product(
        db,
        request.dict()
    )

def get_products(
    db: Session,
    limit: int,
    cursor: str = None,
    search: str = None,
    category: str = None,
    min_price: float = None,
    max_price: float = None,
    sort_by: str = "created_at",
    sort_order: str = "desc"
):

    products = crud.get_products(
        db=db,
        limit=limit,
        cursor=cursor,
        search=search,
        category=category,
        min_price=min_price,
        max_price=max_price,
        sort_by=sort_by,
        sort_order=sort_order
    )

    # IMPORTANT: determine has_more BEFORE slicing
    has_more = len(products) > limit

    # slice only after determining has_more
    products_to_return = products[:limit]

    next_cursor = None

    if has_more:

        last_product = products_to_return[-1]

        next_cursor = encode_cursor(
            last_product.created_at,
            last_product.id
        )

    return {
        "data": products_to_return,
        "next_cursor": next_cursor,
        "has_more": has_more
    }

def get_product_by_id(
    db: Session,
    product_id: int
):

    return crud.get_product_by_id(
        db,
        product_id
    )


def update_product(
    db: Session,
    product_id: int,
    request: ProductCreate
):

    product = crud.get_product_by_id(
        db,
        product_id
    )

    return crud.update_product(
        db,
        product,
        request.dict()
    )


def delete_product(
    db: Session,
    product_id: int
):

    product = crud.get_product_by_id(
        db,
        product_id
    )

    crud.soft_delete_product(
        db,
        product
    )
