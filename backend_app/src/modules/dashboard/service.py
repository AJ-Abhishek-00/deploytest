from sqlalchemy.orm import Session

from src.modules.dashboard import crud


def get_dashboard_summary(db: Session):

    total_products = crud.get_total_products(db)

    average_rating = crud.get_average_rating(db)

    highest_priced_product = crud.get_highest_priced_product(db)

    recent_products = crud.get_recent_products(db)

    return {
        "total_products": total_products,
        "average_rating": average_rating,
        "highest_priced_product": highest_priced_product,
        "recent_products": recent_products
    }
