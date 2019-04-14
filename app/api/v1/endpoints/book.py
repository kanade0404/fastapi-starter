import requests
import json
from fastapi import APIRouter, Query, Security
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import or_, and_
from starlette.responses import JSONResponse
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from app.db.base import session
from app.db_model.book import BookTable
from app.model.book import Book, SearchCondBook
from app.api.utils.book import call_api, convert_api_data


router = APIRouter()

oauth_scheme = OAuth2PasswordBearer(tokenUrl="/token")


@router.get("/book/", tags=["book"])
def find_book_from_openbd(token: str = Security(oauth_scheme),
                          isbn: str = Query(..., alias='isbn-app', max_length=13)):
    try:
        data = call_api(isbn)
        if data[0] == None:
            raise ValueError
        response_data = convert_api_data(data[0])
    except Exception as e:
        return JSONResponse(status_code=HTTP_400_BAD_REQUEST, content={'error': e})
    return JSONResponse(status_code=HTTP_200_OK, content=response_data)


@router.get("/book/", tags=["book"], response_model=SearchCondBook)
def find_book_by_isbn(search_cond: SearchCondBook):
    try:
        query = session.query(BookTable)
        filters = list()
        for cond in search_cond:
            if cond:
                filters.append(and_())
        book = session.query(BookTable).filter()
    except Exception as e:
        return JSONResponse(status_code=HTTP_400_BAD_REQUEST, content=e)
    return JSONResponse(status_code=HTTP_200_OK, content=book)


@router.post("/book/", tags=["book"], response_model=Book)
def create_book(response_book: Book):
    book = BookTable()
    book.isbn = response_book.isbn
    book.title = response_book.title
    book.publisher = response_book.publisher
    book.author = response_book.author
    book.cover = response_book.cover
    book.publish_date = response_book.publish_date
    try:
        session.add(book)
        session.commit()
    except Exception as e:
        return JSONResponse(status_code=HTTP_400_BAD_REQUEST, content={'error': e})
    return JSONResponse(status_code=HTTP_201_CREATED, content=response_book)
