from sqlalchemy import  Table, Column, Integer, Float, String, Text

from src.database import metadata

product = Table(
    'product',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False, unique=True),
    Column('description', Text),
    Column('price', Float, nullable=False),
    Column('quantity', Integer, nullable=False)
)