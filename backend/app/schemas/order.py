from pydantic import BaseModel
from datetime import datetime
from typing import List

from .order_item import OrderItemRead

class OrderBase(BaseModel):
    customer_id: int
    total_amount: float

class OrderCreate(OrderBase):
    items: List[OrderItemRead]

class OrderRead(OrderBase):
    id: int
    bot_id: int
    status: str
    created_at: datetime
    updated_at: datetime
    items: List[OrderItemRead]

    class Config:
        orm_mode = True
