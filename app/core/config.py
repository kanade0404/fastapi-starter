import os

API_V1_STR = '/api/v1'
MYSQL_USER_NAME = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_DB_NAME = os.getenv('MYSQL_DATABASE')
MYSQL_ROOT_PASSWORD = os.getenv('MYSQL_ROOT_PASSWORD')
HOST_NAME = os.getenv('HOST_NAME')
SECRET_KEY = os.getenv('SECRET_KEY')
if not SECRET_KEY:
    SECRET_KEY = os.urandom(32)
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_SUBJECT = os.getenv('ACCESS_TOKEN_SUBJECT')
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 8