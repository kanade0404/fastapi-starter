import jwt
from jwt import PyJWTError
from fastapi import Security, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from starlette.status import HTTP_403_FORBIDDEN
from sqlalchemy.orm import Session
from .db import get_db
from ...core import config
from ...crud.user import find, is_active
from ...db_model.user import UserTable
from ...model.token import TokenPayload

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login/access-token")


def get_current_user(db_session: Session = Depends(get_db), token: str = Security(oauth2_scheme)):
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
        token_data = TokenPayload(**payload)
    except PyJWTError:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN,
            detail='Could not validate credentials.'
        )
    user = find(db_session=db_session, user_id=token_data.user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail='User not found.'
        )
    return user


def get_current_active_user(current_user: UserTable = Security(get_current_user)):
    if not is_active(current_user):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
