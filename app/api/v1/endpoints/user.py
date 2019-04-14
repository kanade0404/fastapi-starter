from fastapi import Query, Path, APIRouter, HTTPException, Depends, Security
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from app.api.utils.db import get_db
from app.api.utils.security import get_current_active_user
from app.crud.user import create, find, find_by_email
from app.db.base import session
from app.db_model.user import UserTable
from app.model.user import User, UserInCreate, CurrentUser


router = APIRouter()

# ----------APIの定義------------
# idにマッチするユーザ情報を取得 GET
@router.get("/user/{user_id}", tags=["user"], response_model=User)
async def read_user(user_id: int = Path(..., gt=0)):
    try:
        user = find(db_session=session, user_id=user_id)
    except Exception as e:
        return JSONResponse(status_code=HTTP_400_BAD_REQUEST, content={'error': e})
    return JSONResponse(status_code=HTTP_200_OK, content=user)

# ユーザ情報を登録 POST
@router.post("/user/", tags=["user"], response_model=User)
# クエリでnameとstrを受け取る
async def create_user(response_user: UserInCreate):
    try:
        user = find_by_email(db_session=session, email=response_user.email)
        if user:
            raise HTTPException(status_code=400,
                                detail="The user with this username already exists in the system.")
        user = create(db_session=session, user_in=response_user)
    except Exception as e:
        return JSONResponse(status_code=HTTP_400_BAD_REQUEST, content={'error': e})
    return JSONResponse(status_code=HTTP_201_CREATED, content=user)


@router.get("/user/me", tags=["user"], response_model=User)
async def read_users_me(db: Session = Depends(get_db), current_user: UserTable = Depends(get_current_active_user)):
    return current_user

