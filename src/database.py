from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAMEDB

SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAMEDB}"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
session_maker = sessionmaker(engine, autoflush=False)

def get_session():
    with session_maker() as session:
        yield session



