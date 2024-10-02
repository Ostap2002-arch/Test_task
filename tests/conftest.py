import pytest
from config import DB_HOST_TEST, DB_NAME_TEST, DB_PASS_TEST, DB_PORT_TEST, DB_USER_TEST
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from main import app
from products.models import metadata
from database import get_session

DATABASE_URL_TEST = f"postgresql://{DB_USER_TEST}:{DB_PASS_TEST}@{DB_HOST_TEST}:{DB_PORT_TEST}/{DB_NAME_TEST}"


engine_test = create_engine(DATABASE_URL_TEST)
metadata.bind = engine_test
session_maker = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)


def get_test_session():
    with session_maker() as session:
        yield session


app.dependency_overrides[get_session] = get_test_session


@pytest.fixture(autouse=True, scope='session')
def prepare_database():
    metadata.create_all(engine_test)
    yield
    metadata.drop_all(engine_test)


client = TestClient(app)

# @pytest.fixture(autouse=True, scope='session')
# async def prepare_database():
#     with engine_test.begin() as conn:
#         conn.run(metadata.create_all)
#     yield
#     with engine_test.begin() as conn:
#         conn.run(metadata.drop_all)

# @pytest.fixture(scope='session')
# def event_loop(request):
#     loop = asyncio.get_event_loop_policy().new_event_loop()
#     yield loop
#     loop.close()
