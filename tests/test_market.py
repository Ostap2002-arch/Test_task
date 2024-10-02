import json
import logging
from datetime import datetime, date
from conftest import client

logging.basicConfig(level=logging.DEBUG)

# Test data
tea = {
    "name": "tea",
    "description": "green tea",
    "price": 10.00,
    "quantity": 138
}

milk = {
    'name': "milk",
    "description": "green tea",
    "price": 12.50,
    "quantity": 250
}

elem_order = {
    "product": "milk",
    "total": 100
}

new_status = {
    "status": "sent"
}


# Test create product
def test_create_product():
    response = client.post("/products/", json=tea)
    logging.info("Это информационное сообщение")
    assert response.status_code == 201


# Test get all product
def test_show_all_products():
    response = client.get("/products/")
    logging.info("Это информационное сообщение")
    assert response.status_code == 200
    assert len(response.json()) == 1


# Test get info about tea
def test_info_product():
    response = client.get("/products/1")
    logging.info("Это информационное сообщение")
    assert response.status_code == 200
    assert json.loads(response.text) == tea


# Test update product
def test_change_product():
    response = client.put("/products/1", json=milk)
    logging.info("Это информационное сообщение")
    assert response.status_code == 200
    response_info = client.get("/products/1")
    assert json.loads(response_info.text) == milk


# Test create order
def test_create_order():
    response = client.post("/orders/", json=[elem_order])
    logging.info("Это информационное сообщение")
    assert response.status_code == 201


# Test get order
def test_info_order():
    response = client.get("/orders/1")
    logging.info("Это информационное сообщение")
    assert response.status_code == 200
    assert response.json()['order_items'][0] == elem_order
    assert datetime.fromisoformat(response.json()['date_create']).date() == date.today()
    assert response.json()['status'] == 'in_progress'


# Test get all order
def test_Show_all_orders():
    response = client.get("/orders/")
    logging.info("Это информационное сообщение")
    assert response.status_code == 200
    assert len(response.json()) == 1


# Test update status
def test_change_status():
    response = client.patch('/orders/1/status', json=new_status)
    logging.info("Это информационное сообщение")
    assert response.status_code == 201
    response = client.get("/orders/1")
    assert response.json()['status'] == 'sent'


