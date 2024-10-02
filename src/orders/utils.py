# from src.database import SessionLocal
from sqlalchemy import select
from src.orders.models import orderitem
from src.products.models import product
from src.orders.models import order


def get_order(ord, session):
    query = select(orderitem).where(orderitem.c.id_order == ord.id)
    list_item = session.execute(query).all()
    dict_order = {'id': ord.id, 'date_create': ord.date_create.isoformat(), 'status': ord.status}
    dict_order.update(order_items=[])
    for item in list_item:
        query = select(product).where(product.c.id == item.id_product)
        product_from_item = session.execute(query).first()
        dict_item = {'product': product_from_item.name, 'total': item.totla}
        dict_order['order_items'].append(dict_item)
    return dict_order

def check_order_availability(id_order: int, session):
    query = select(order).where(order.c.id == id_order)
    ord = session.execute(query).first()
    return bool(ord)