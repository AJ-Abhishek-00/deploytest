from sqlalchemy.orm import Session
from sqlalchemy import func, desc

from src.modules.product.model import Product


def get_total_products(db: Session):

    return db.query(func.count(Product.id)).filter(
        Product.is_deleted == False
    ).scalar()


def get_average_rating(db: Session):

    return db.query(func.avg(Product.rating)).filter(
        Product.is_deleted == False
    ).scalar()


def get_highest_priced_product(db: Session):

    return db.query(Product).filter(
        Product.is_deleted == False
    ).order_by(desc(Product.price)).first()


def get_recent_products(db: Session, limit: int = 5):

    return db.query(Product).filter(
        Product.is_deleted == False
    ).order_by(desc(Product.created_at)).limit(limit).all()
