from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from src.modules.user.schema import UserResponse
from src.modules.user.service import get_users, get_user

from src.core.db.session import get_db


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("", response_model=List[UserResponse])
def list_users(
    db: Session = Depends(get_db)
):

    return get_users(db)


@router.get("/{user_id}", response_model=UserResponse)
def get_single_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    return get_user(db, user_id)
