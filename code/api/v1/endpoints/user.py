from fastapi import Query, Path, APIRouter
from typing import List
from code.db.base import session
from code.db_model.user import UserTable
from code.model.user import User, UserInCreate


router = APIRouter()

# ----------APIの定義------------
# テーブルにいる全ユーザ情報を取得 GET
@router.get("user/", tags=["user"], response_model=List[User])
def read_users():
    users = session.query(UserTable).all()
    return users

# idにマッチするユーザ情報を取得 GET
@router.get("user/{user_id}", tags=["user"], response_model=User)
def read_user(user_id: int):
    user = session.query(UserTable).\
        filter(UserTable.id == user_id).first()
    return user

# ユーザ情報を登録 POST
@router.post("/user/", tags=["user"], response_model=User)
# クエリでnameとstrを受け取る
async def create_user(response_user: UserInCreate):
    user = UserTable()
    user.name = response_user.name
    user.email = response_user.email
    user.password = response_user.password
    session.add(user)
    session.commit()

# ユーザ情報を更新 PUT
@router.put("/user/", tags=["user"], response_model=User)
# modelで定義したUserモデルのリクエストbodyをリストに入れた形で受け取る
async def update_users(response_user: User):
    user = session.query(UserTable).filter(UserTable.id == response_user.id).first()
    if not user:
        raise ValueError
    user.name = response_user.name
    user.age = response_user.age
    session.commit()
