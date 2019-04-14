from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.api.utils.db import get_db
from app.crud.user import authenticate, is_active
from app.model.token import Token
from app.core import config
from app.core.jwt import create_access_token

router = APIRouter()


@router.post("/login/access-token", response_model=Token, tags=["login"])
def login_access_token(db: Session = Depends(get_db),
                       form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate(
        db_session=db, email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": create_access_token(
            data={"user_id": user.id},
            expires_delta=access_token_expires
        ),
        "token_type": "bearer"
    }
