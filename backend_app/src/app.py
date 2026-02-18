from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from src.core.db.session import SessionLocal
from src.modules.product.model import Product

# Create FastAPI app
app = FastAPI()

# ✅ Root route
@app.get("/")
def root():
    return {"message": "Backend is running successfully 🚀"}

# ✅ CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import routers
from src.modules.auth.router import router as auth_router
from src.modules.product.router import router as product_router
from src.modules.dashboard.router import router as dashboard_router

# Include routers
app.include_router(auth_router)
app.include_router(product_router)
app.include_router(dashboard_router)


# ✅ Auto Seed 50 Products On Startup
@app.on_event("startup")
def seed_products():

    db: Session = SessionLocal()

    try:
        # If products already exist, do nothing
        if db.query(Product).count() > 0:
            return

        # Insert 50 default products
        for i in range(1, 51):
            product = Product(
                name=f"Sample Product {i}",
                category="General",
                price=100 + i,
                rating=4.0
            )
            db.add(product)

        db.commit()

        print("✅ 50 products seeded successfully")

    finally:
        db.close()
