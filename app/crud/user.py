from typing import Optional
from sqlalchemy import and_
from ..core.security import get_password_hash, verify_password
from ..db.base import session
from ..db_model.user import UserTable
from ..model.user import UserInCreate


def find(db_session: session, *, user_id: int) -> Optional[UserTable]:
    return db_session.query(UserTable).filter(
        and_(UserTable.id == user_id, UserTable.is_active))


def find_by_email(db_session: session, *, email: str) -> Optional[UserTable]:
    return db_session.query(UserTable).filter(
        and_(UserTable.email == email, UserTable.is_active))


def authenticate(db_session: session, *, email: str, password: str) -> Optional[UserTable]:
    user = find_by_email(db_session=db_session, email=email)
    if not user:
        return None
    if not verify_password(plain_password=password, hashed_password=user.password):
        return None
    return user


def create(db_session: session, *, user_in: UserInCreate) -> UserTable:
    user = UserTable(name=user_in.name,
                     email=user_in.email,
                     password=get_password_hash(user_in.password))
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user


def is_active(user: UserTable) -> bool:
    return user.is_active
