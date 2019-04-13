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
    age: int = Schema(None,
                      title='The user age',
                      description='This is the user age.')
    created_at: datetime = Schema(datetime.now(),
                                  title='The created datetime',
                                  description='This is the created user datetime.')


class UserInCreate(User):
    """
    Create UserInfo Model
    """
    password: str = Schema(..., title='The user password', description='This is the user hashed password.')
