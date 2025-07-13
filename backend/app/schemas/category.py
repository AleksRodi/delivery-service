from pydantic import BaseModel
from typing import Optional

class CategoryBase(BaseModel):
    name: str
    sort_order: Optional[int] = 0

class CategoryCreate(CategoryBase):
    pass

class CategoryRead(CategoryBase):
    id: int

    class Config:
        orm_mode = True
