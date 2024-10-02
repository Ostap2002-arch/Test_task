from sqlalchemy import MetaData, Table, Column, Integer, Float, String, Text, DateTime, ForeignKey

metadata = MetaData()

product = Table(
    'product',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False, unique=True),
    Column('description', Text),
    Column('price', Float, nullable=False),
    Column('quantity', Integer, nullable=False)
)