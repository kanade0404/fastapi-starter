from sqlalchemy import Column, Integer, String
from ..db.base import Base


class BookTable(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    isbn = Column(String(13), nullable=False)
    title = Column(String(100), nullable=False)
    author = Column(String(100), nullable=False)
    publisher = Column(String(100), nullable=False)
    cover = Column(String(255), nullable=True)
    publish_date = Column(Integer, nullable=True)
