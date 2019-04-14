from fastapi import APIRouter
from ...api.v1.endpoints import user, book, comment

api_router = APIRouter()
api_router.include_router(user.router)
api_router.include_router(book.router)
