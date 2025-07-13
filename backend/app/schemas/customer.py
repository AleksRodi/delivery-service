from pydantic import BaseModel
from typing import Optional

class CustomerBase(BaseModel):
    telegram_user_id: str
    name: Optional[str]
    phone: Optional[str]
    address: Optional[str]

class CustomerCreate(CustomerBase):
    bot_id: int

class CustomerRead(CustomerBase):
    id: int
    bot_id: int

    class Config:
        orm_mode = True
