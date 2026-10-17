from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate


def create_user(db: Session, user_data: UserCreate) -> User:
    user = User(
        name=user_data.name,
        email=str(user_data.email),
    )

    try:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    except IntegrityError as exc:
        db.rollback()
        raise ValueError(
            "A user with this email already exists."
        ) from exc


def get_user(db: Session, user_id: int) -> User | None:
    statement = select(User).where(User.id == user_id)

    return db.scalars(statement).first()