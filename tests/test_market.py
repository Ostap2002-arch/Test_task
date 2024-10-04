import json
import logging
from datetime import datetime, date
from conftest import client


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

id_product = '0'
id_order = '0'
# Test create product
def test_create_product():
    response = client.post("/products/", json=tea)
    id = str(response.text.split()[-1])
    global id_product
    id_product = id
    assert response.status_code == 201


# Test get all product
def test_show_all_products():
    response = client.get("/products/")
    assert response.status_code == 200
    assert len(response.json()) == 1


# Test get info about tea
def test_info_product():
    response = client.get(f"/products/{id_product}")
    assert response.status_code == 200
    assert json.loads(response.text) == tea


# Test update product
def test_change_product():
    response = client.put(f"/products/{id_product}", json=milk)
    assert response.status_code == 200
    response_info = client.get(f"/products/{id_product}")
    assert json.loads(response_info.text) == milk


# Test create order
def test_create_order():
    response = client.post("/orders/", json=[elem_order])
    global id_order
    id_order = response.text.split()[-1]
    assert response.status_code == 201


# Test get order
def test_info_order():
    response = client.get(f"/orders/{id_order}")
    assert response.status_code == 200
    assert response.json()['order_items'][0] == elem_order
    assert datetime.fromisoformat(response.json()['date_create']).date() == date.today()
    assert response.json()['status'] == 'in_progress'


# Test get all order
def test_Show_all_orders():
    response = client.get("/orders/")
    assert response.status_code == 200
    assert len(response.json()) == 1


# Test update status
def test_change_status():
    response = client.patch(f'/orders/{id_order}/status', json=new_status)
    assert response.status_code == 201
    response = client.get(f"/orders/{id_order}")
    assert response.json()['status'] == 'sent'