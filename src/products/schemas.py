from typing import Union, Text, Optional
from fastapi import Query
from pydantic import BaseModel


class Products(BaseModel):
    name: str
    description: Union[Text, None] = None
    price: float = Query(gt=0)
    quantity: int = Query(ge=0)

class Change_product(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = Query(None, gt=0)
    quantity: Optional[int] = Query(None, ge=0)