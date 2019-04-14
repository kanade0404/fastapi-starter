from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware  # CORSを回避するために必要
from db.base import Base, ENGINE  # DBと接続するためのセッション
from core import config
from api.v1.api import api_router

app = FastAPI()

# CORSを回避するために設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=config.API_V1_STR)


if __name__ == '__main__':
    Base.metadata.create_all(bind=ENGINE)
