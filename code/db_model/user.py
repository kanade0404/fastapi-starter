from _datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from code.db.base import Base


class UserTable(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    age = Column(Integer, nullable=True)
