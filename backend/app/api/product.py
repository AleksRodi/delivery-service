from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.product import ProductRead, ProductCreate
from app.crud.product import get_product_by_id, list_products_by_category, create_product, delete_product
from app.db.session import get_db

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/", response_model=ProductRead, status_code=status.HTTP_201_CREATED)
async def register_product(
    product: ProductCreate,
    db: AsyncSession = Depends(get_db),
):
    created_product = await create_product(db, product)
    if not created_product:
        raise HTTPException(status_code=400, detail="Product not created")
    return created_product

@router.get("/", response_model=List[ProductRead])
async def read_products(
    category_id: int,
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
):
    products = await list_products_by_category(db, category_id, skip=skip, limit=limit)
    return products

@router.get("/{product_id}", response_model=ProductRead)
async def read_product(product_id: int, db: AsyncSession = Depends(get_db)):
    product = await get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.delete("/{product_id}", response_model=ProductRead)
async def remove_product(product_id: int, db: AsyncSession = Depends(get_db)):
    product = await delete_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
