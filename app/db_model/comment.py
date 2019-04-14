from _datetime import datetime
from sqlalchemy import Column, Integer, DateTime, Text, ForeignKey
from app.db.base import Base


class CommentTable(Base):
    __tablename__ = 'comments'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    content = Column('content', Text, nullable=False)
    user = Column('user_id', Integer, ForeignKey('user.id'), nullable=False)
    book = Column('book_id', Integer, ForeignKey('book.id'), nullable=False)
    created_at = Column('created_at', DateTime, default=datetime.now, nullable=False)
