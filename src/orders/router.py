from http import HTTPStatus
from typing import List
from fastapi import APIRouter, HTTPException, Depends
from src.orders.schemas import Order_Item
from src.database import get_session
from sqlalchemy import insert, select, update
from src.orders.models import order, orderitem
from src.products.models import product
from src.orders.schemas import Order
from src.orders.utils import get_order
from src.orders.schemas import Status
from src.products.utils import get_product_from_list
from fastapi.responses import Response
from src.orders.utils import check_order_availability

router = APIRouter(
    prefix='/orders',
    tags=['Orders']
)


@router.post('/', tags=['CRUD_order'], description="Creating an order")
def create_order(list_item: List[Order_Item], session = Depends(get_session)):
    dict_id_product = dict()
    # Сhecking list_item for correctness
    for item in list_item:
        # Getting a product from the list
        # Using a function from the utils module
        product_from_list = get_product_from_list(item, session)
        # Сhecking for total
        if item.total > product_from_list.quantity:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=f"Недостаточно {item.product} на складе")
        # If everything is fine
        dict_id_product.update([(item.product, product_from_list.id)])

    # Create and get new_order
    stmt = insert(order).values().returning(order)
    result = session.execute(stmt)
    new_order_id = result.fetchone().id

    # Crete order_item
    for item in list_item:
        #Changing the number of products in stock
        #Step 1 - receive the product
        # Using a function from the utils module
        product_from_list = get_product_from_list(item, session)
        #Step 2 -changing the quantity
        stmt = update(product).where(product.c.id == product_from_list.id).values(quantity = product_from_list.quantity - item.total)
        session.execute(stmt)
        session.commit()
        #Step 3 - create order item
        stmt = insert(orderitem).values(id_order=new_order_id, id_product=dict_id_product.get(item.product),
                                        totla=item.total)
        session.execute(stmt)
        session.commit()
    return Response(content=f"Order successfully created, number {new_order_id}", media_type="text/plain", status_code=201)


@router.get('/', response_model=List[Order], tags=['order'], description="Getting a list of orders")
def Show_all_orders(session = Depends(get_session)):
    # Create result list
    result = list()

    # Getting all orders
    query = select(order)
    list_order = session.execute(query).all()
    for ord in list_order:
        # Getting info about ord
        dict_order = get_order(ord, session)
        result.append(dict_order)
    return result


@router.get('/{id}', response_model=Order, tags=['order'], description="Getting information about an order by its id")
def info_order(id: int, session = Depends(get_session)):
    if check_order_availability(id, session):
        query = select(order).where(order.c.id == id)
        ord = session.execute(query).first()
        return get_order(ord, session)
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=f"Заказ не найден")



@router.patch('/{id}/status', tags=['CRUD_order'], description="Change the status of an order with a given id (in)")
def change_status(id: int, status: Status, session = Depends(get_session)):
    if check_order_availability(id, session):
        stmt = update(order).where(order.c.id == id).values(status = status.status.name)
        session.execute(stmt)
        session.commit()
        return Response(content=f"Status has been updated", media_type="text/plain", status_code=201)
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=f"Заказ не найден")
