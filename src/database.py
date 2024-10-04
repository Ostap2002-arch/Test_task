from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

from src.config import settings

SQLALCHEMY_DATABASE_URL = settings.DB_URL

metadata = MetaData()
engine = create_engine(SQLALCHEMY_DATABASE_URL)
session_maker = sessionmaker(engine, autoflush=False)

def get_session():
    with session_maker() as session:
        yield session


def clear_db():
    metadata_clear = MetaData()
    metadata_clear.bind = engine
    metadata_clear.reflect(bind=engine)
    for table in metadata_clear.tables.values():
        if table.name == 'alembic_version':
            continue
        if table.name == 'orderitem':
            session = next(get_session())
            session.execute(table.delete())
            session.commit()
            session.close()
            continue
        continue
    for table in metadata_clear.tables.values():
        if table.name == 'alembic_version':
            continue
        session = next(get_session())
        session.execute(table.delete())
        session.commit()
        session.close()


