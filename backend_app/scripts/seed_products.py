from src.core.db.session import SessionLocal
from src.modules.product.model import Product

db = SessionLocal()

categories = [
    "Electronics",
    "Clothing",
    "Books",
    "Home",
    "Sports"
]

for i in range(1, 101):

    product = Product(

        name=f"Product {i}",

        category=categories[i % 5],

        price=100 + i * 10,

        rating=3.5 + (i % 5) * 0.5

    )

    db.add(product)

db.commit()

print("100 products inserted successfully")
