import sys

from fastapi import FastAPI
from src.products.router import router as router_products
from src.orders.router import router as router_orders
description = """
This API is a tests task for the company Effective Mobile, and is a mini application for placing orders.
## In it you can:
* **Create and edit products**
* **Create and edit orders**
"""
print(sys.path)
tags_metadata = [
    {
        "name": "product",
        "description": "Obtaining information about a product or products",
    },
    {
        "name" : "CRUD_product",
        "description" : "CRUD operations on a product or products ",
    },
    {
        "name" : "order",
        "description" : "Obtaining information about a order or orders ",
    },
    {
        "name" : "CRUD_order",
        "description" : "CRUD operations on a order or orders ",
    },
]
app = FastAPI(title="Market",
              description=description,
              version="0.115.0",
              contact={
                  "name": "Ostap",
                  "url": "https://vk.com/id207571262",
                  "email": "yevstafiyt2021@mail.ru",
              },
              openapi_tags=tags_metadata
              )


#Include routers
app.include_router(router_products)
app.include_router(router_orders)










