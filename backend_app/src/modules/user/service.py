from sqlalchemy.orm import Session

from src.modules.user import crud


def get_users(db: Session):

    return crud.get_all_users(db)


def get_user(db: Session, user_id: int):

    return crud.get_user_by_id(db, user_id)


def change_user_role(
    db: Session,
    user_id: int,
    role: str
):

    user = crud.get_user_by_id(db, user_id)

    return crud.update_user_role(db, user, role)
