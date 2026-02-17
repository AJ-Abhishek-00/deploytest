from sqlalchemy.orm import Session
from sqlalchemy import and_, or_

from src.modules.product.model import Product
from src.utils.pagination import decode_cursor


# CREATE PRODUCT
def create_product(
    db: Session,
    product_data: dict
):

    product = Product(**product_data)

    db.add(product)

    db.commit()

    db.refresh(product)

    return product


# GET SINGLE PRODUCT
def get_product_by_id(
    db: Session,
    product_id: int
):

    return db.query(Product).filter(
        Product.id == product_id,
        Product.is_deleted == False
    ).first()


# GET PRODUCTS WITH CURSOR PAGINATION
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

    query = db.query(Product).filter(
        Product.is_deleted == False
    )

    # SEARCH FILTER
    if search:

        query = query.filter(
            Product.name.ilike(f"%{search}%")
        )

    # CATEGORY FILTER
    if category:

        query = query.filter(
            Product.category == category
        )

    # PRICE FILTERS
    if min_price is not None:

        query = query.filter(
            Product.price >= min_price
        )

    if max_price is not None:

        query = query.filter(
            Product.price <= max_price
        )

    # CURSOR FILTER (CRITICAL FIX)
    if cursor:

        decoded = decode_cursor(cursor)

        cursor_created_at = decoded["created_at"]
        cursor_id = decoded["id"]

        if sort_order == "desc":

            query = query.filter(

                or_(

                    Product.created_at < cursor_created_at,

                    and_(

                        Product.created_at == cursor_created_at,
                        Product.id < cursor_id

                    )

                )

            )

        else:

            query = query.filter(

                or_(

                    Product.created_at > cursor_created_at,

                    and_(

                        Product.created_at == cursor_created_at,
                        Product.id > cursor_id

                    )

                )

            )

    # SORTING
    sort_column = getattr(Product, sort_by)

    if sort_order == "desc":

        query = query.order_by(
            sort_column.desc(),
            Product.id.desc()
        )

    else:

        query = query.order_by(
            sort_column.asc(),
            Product.id.asc()
        )

    # FETCH limit + 1 FOR has_more LOGIC
    products = query.limit(limit + 1).all()

    return products


# UPDATE PRODUCT
def update_product(
    db: Session,
    product,
    update_data: dict
):

    for key, value in update_data.items():

        setattr(product, key, value)

    db.commit()

    db.refresh(product)

    return product


# SOFT DELETE PRODUCT
def soft_delete_product(
    db: Session,
    product
):

    product.is_deleted = True

    db.commit()
