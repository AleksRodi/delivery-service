from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.category import CategoryRead, CategoryCreate
from app.crud.category import (
    get_category_by_id,
    list_categories_by_bot,
    create_category,
    delete_category
)
from app.db.session import get_db

router = APIRouter(prefix="/categories", tags=["categories"])

@router.post("/", response_model=CategoryRead, status_code=status.HTTP_201_CREATED)
async def register_category(
    category: CategoryCreate,
    bot_id: int,  # Можно брать из токена бота, если будет авторизация
    db: AsyncSession = Depends(get_db),
):
    created_category = await create_category(db, bot_id, category)
    if not created_category:
        raise HTTPException(status_code=400, detail="Category not created")
    return created_category

@router.get("/", response_model=List[CategoryRead])
async def read_categories(
    bot_id: int,
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
):
    categories = await list_categories_by_bot(db, bot_id, skip=skip, limit=limit)
    return categories

@router.get("/{category_id}", response_model=CategoryRead)
async def read_category(category_id: int, db: AsyncSession = Depends(get_db)):
    category = await get_category_by_id(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.delete("/{category_id}", response_model=CategoryRead)
async def remove_category(category_id: int, db: AsyncSession = Depends(get_db)):
    category = await delete_category(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category
