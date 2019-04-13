from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware  # CORSを回避するために必要
from code.db.base import Base, ENGINE  # DBと接続するためのセッション

app = FastAPI()

# CORSを回避するために設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router()


if __name__ == '__main__':
    Base.metadata.create_all(bind=ENGINE)
