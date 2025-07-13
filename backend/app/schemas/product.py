from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    image_url: Optional[str] = None
    is_available: Optional[bool] = True
    sort_order: Optional[int] = 0

class ProductCreate(ProductBase):
    category_id: int

class ProductRead(ProductBase):
    id: int
    category_id: int

    class Config:
        orm_mode = True
