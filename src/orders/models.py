import datetime
import os
import sys

from sqlalchemy import MetaData, Table, Column, Integer, Float, String, Text, DateTime, ForeignKey
sys.path.append(os.path.abspath('./'))
from src.products.models import metadata

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
