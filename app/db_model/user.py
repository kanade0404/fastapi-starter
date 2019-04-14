from _datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from app.db.base import Base


class UserTable(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(30), nullable=False)
    email = Column('email', String(255), nullable=False, unique=True)
    password = Column('password', String(255), nullable=False)
    is_active = Column('is_active', Boolean, nullable=False, default=True)
    created_at = Column('created_at', DateTime, default=datetime.now, nullable=False)
