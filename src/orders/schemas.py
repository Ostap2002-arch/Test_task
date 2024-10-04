from datetime import datetime
from enum import Enum
from typing import List, Optional
from fastapi import Query
from pydantic import BaseModel



class Order_Item(BaseModel):
    #Getting available products
    # product: Literal[*get_all_name_product()] - Не работает для тестов
    product: str
    total:int = Query(gt=0)

class SatusModel(str, Enum):
    in_progress = 'in_progress'
    sent = 'sent'
    delivered = 'delivered'


class Order(BaseModel):
    id: int
    date_create: datetime
    status : SatusModel
    order_items: List[Order_Item]

class Status(BaseModel):
    status: Optional[SatusModel] = 'in_progress'
