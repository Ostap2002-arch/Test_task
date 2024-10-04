import datetime
import os
import sys
from sqlalchemy import Table, Column, Integer,  String,  DateTime, ForeignKey
from src.database import metadata

sys.path.append(os.path.abspath('./'))


order = Table(
    'order',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('date_create', DateTime, nullable=False, default=datetime.date.today),
    Column('status', String, nullable=False, default='in_progress'),
)

orderitem = Table(
    'orderitem',
    metadata,
    Column('id_order', Integer, ForeignKey('order.id')),
    Column('id_product', Integer, ForeignKey('product.id')),
    Column('totla', Integer, nullable=False),
)
