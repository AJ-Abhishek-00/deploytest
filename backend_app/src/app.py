from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI app
app = FastAPI()

# ADD CORS HERE
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
