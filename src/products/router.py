from http import HTTPStatus
from typing import List
from fastapi.responses import Response
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm import Session

from src.database import get_session
from src.products.models import product
from src.products.schemas import Products, Change_product

from src.products.utils import check_product_availability

router = APIRouter(
    prefix='/products',
    tags=['Products']
)


@router.get('/', response_model=List[Products], tags=['product'], description = "Getting a list of all products")
def show_all_products(session = Depends(get_session)):
    query = select(product)
    result = session.execute(query).all()
    return result


@router.post('/', tags=['CRUD_product'], description="Creating a new product")
def create_product(new_product: Products, session = Depends(get_session)):
    stmt = insert(product).values(**new_product.dict()).returning(product)
    result = session.execute(stmt)
    id = result.fetchone().id
    session.commit()
    return Response(content=f"The product has been added, number {id}", media_type="text/plain", status_code=201)


@router.get('/{id}/', response_model=Products, tags=['product'], description = "Getting information about a product by its id")
def info_product(id: int, session = Depends(get_session)):
    if check_product_availability(id, session):
        query = select(product).where(product.c.id == id)
        result = session.execute(query).first()
        return result
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Product not found")


@router.put('/{id}/', tags=['CRUD_product'], description="Change product with given id")
def change_product(id: int, new_data: Change_product, session = Depends(get_session)):
    if check_product_availability(id, session):
        query = update(product).where(product.c.id == id)
        new_data = {key: value for key, value in new_data.dict().items() if value is not None}
        session.execute(query, [new_data])
        session.commit()
        return Response(content="The product has been updated", media_type="text/plain", status_code=200)
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Product not found")


@router.delete('/{id}/', tags=['CRUD_product'], description="Removing a product with this id")
def delete_product(id: int, session = Depends(get_session)):
    if check_product_availability(id, session):
        query = delete(product).where(product.c.id == id)
        session.execute(query)
        session.commit()
        return Response(content="The product has been deleted", media_type="text/plain", status_code=200)
    else:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Product not found")
