from itertools import chain
from src.database import get_session
from sqlalchemy import select

from src.products.models import product


def get_product_from_list(item, session):
    query = select(product).where(product.c.name == item.product)
    product_from_list = session.execute(query).first()
    return product_from_list


def check_product_availability(id_product: int, session):
    query = select(product).where(product.c.id == id_product)
    result = session.execute(query).first()
    return bool(result)


def get_all_name_product(session):
    query = select(product.c.name)
    result = session.execute(query).all()
    return [name for name in chain.from_iterable(result)]
