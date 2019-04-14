from pydantic import BaseModel, Schema


class Book(BaseModel):
    id: int = Schema(None, gt=0)
    isbn: str = Schema(..., max_length=13)
    title: str = Schema(..., max_length=100)
    author: str = Schema(..., max_length=100)
    publisher: str = Schema(..., max_length=100)
    cover: str = Schema(None, max_length=255)
    publish_date: int = Schema(..., gt=0)


class SearchCondBook(BaseModel):
    isbn: str = Schema(None, max_length=13)
    title: str = Schema(None, max_length=100)
    author: str = Schema(None, max_length=100)
    publisher: str = Schema(None, max_length=100)
    publish_date_from: int = Schema(None, gt=0)
    publish_date_to: int = Schema(None, gt=0)
