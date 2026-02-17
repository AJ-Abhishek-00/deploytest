from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from typing import Dict

from src.modules.auth import crud
from src.modules.auth.schema import RegisterRequest, LoginRequest

from src.core.security.hashing import hash_password, verify_password
from src.core.security.jwt import (
    create_access_token,
    create_refresh_token,
    decode_token
)


def register_user(
    db: Session,
    request: RegisterRequest
):
    """
    Register a new user with hashed password
    """

    # Check if user already exists
    existing_user = crud.get_user_by_email(
        db,
        request.email
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )

    # Hash password before saving
    hashed_password = hash_password(
        request.password
    )

    # Create user in DB
    user = crud.create_user(
        db=db,
        email=request.email,
        password=hashed_password
    )

    return user


def login_user(
    db: Session,
    request: LoginRequest
) -> Dict[str, str]:
    """
    Authenticate user and generate access + refresh tokens
    """

    user = crud.get_user_by_email(
        db,
        request.email
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    # Verify password
    if not verify_password(
        request.password,
        user.password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    # Create tokens
    access_token = create_access_token(
        data={"user_id": user.id}
    )

    refresh_token = create_refresh_token(
        data={"user_id": user.id}
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }


def refresh_access_token(
    refresh_token: str
) -> Dict[str, str]:
    """
    Generate new access token using refresh token
    """

    try:
        payload = decode_token(refresh_token)

        user_id = payload.get("user_id")

        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid refresh token"
            )

        new_access_token = create_access_token(
            data={"user_id": user_id}
        )

        return {
            "access_token": new_access_token,
            "token_type": "bearer"
        }

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token"
        )


def get_current_user(
    db: Session,
    token: str
):
    """
    Get current user from JWT access token
    """

    try:
        payload = decode_token(token)

        user_id = payload.get("user_id")

        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )

        user = crud.get_user_by_id(
            db,
            user_id
        )

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        return user

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
