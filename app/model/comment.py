from pydantic import BaseModel, Schema
from datetime import datetime
from .user import User
from .book import Book


class Comment(BaseModel):
    id: int = Schema(None, gt=0)
    content: str = Schema(...)
    user: User = Schema(...)
    book: Book = Schema(...)
    created_at: datetime = Schema(datetime.now)
