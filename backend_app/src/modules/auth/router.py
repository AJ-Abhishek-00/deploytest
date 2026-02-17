from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from src.modules.auth.schema import (
    RegisterRequest,
    LoginRequest,
    TokenResponse,
    UserResponse
)

from src.modules.auth.service import (
    register_user,
    login_user,
    get_current_user,
)

from src.core.db.session import get_db


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

# FIX: Use /auth/token instead of /auth/login
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


@router.post("/register", response_model=UserResponse)
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db)
):
    return register_user(db, request)


# Your existing JSON login (keep this)
@router.post("/login", response_model=TokenResponse)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):
    return login_user(db, request)


# NEW: OAuth2 compatible login (REQUIRED for Swagger Authorize)
@router.post("/token", response_model=TokenResponse)
def login_oauth(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """
    OAuth2 login endpoint
    username = email
    password = password
    """

    request = LoginRequest(
        email=form_data.username,
        password=form_data.password
    )

    return login_user(db, request)


@router.get("/me", response_model=UserResponse)
def me(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    """
    Get current logged-in user
    """

    return get_current_user(db, token)
