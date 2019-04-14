from typing import Optional
from pydantic import BaseModel, Schema, EmailStr
from datetime import datetime


class User(BaseModel):
    """
    Base User Model
    """
    id: int = Schema(None,
                     title='The user id',
                     description='This is the user identify.',
                     gt=0)
    name: str = Schema(...,
                       title='The user name',
                       description='This is the user name.')
    email: EmailStr = Schema(...,
                             title='The user email',
                             description='This is the user email.')
    is_active: bool = Schema(True,
                             title='The logic delete flag.',
                             description='This values is False if user is not active.')
    created_at: datetime = Schema(datetime.now,
                                  title='The created datetime',
                                  description='This is the created user datetime.')


class CurrentUser(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    email: Optional[str] = None
    is_active: Optional[bool] = None


class UserInCreate(BaseModel):
    """
    Create UserInfo Model
    """
    id: int = Schema(None,
                     title='The user id',
                     description='This is the user identify.',
                     gt=0)
    name: str = Schema(...,
                       title='The user name',
                       description='This is the user name.')
    email: str = Schema(...,
                        title='The user email',
                        description='This is the user email.')
    password: str = Schema(...,
                           title='The user password',
                           description='This is the user hashed password.')
