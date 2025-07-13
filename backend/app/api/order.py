from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.order import OrderRead, OrderCreate
from app.crud.order import (
    get_order_by_id,
    list_orders_by_bot,
    create_order,
    delete_order
)
from app.db.session import get_db

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/", response_model=OrderRead, status_code=status.HTTP_201_CREATED)
async def register_order(
    order: OrderCreate,
    bot_id: int,
    db: AsyncSession = Depends(get_db),
):
    created_order = await create_order(db, bot_id, order)
    if not created_order:
        raise HTTPException(status_code=400, detail="Order not created")
    return created_order

@router.get("/", response_model=List[OrderRead])
async def read_orders(
    bot_id: int,
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
):
    orders = await list_orders_by_bot(db, bot_id, skip=skip, limit=limit)
    return orders

@router.get("/{order_id}", response_model=OrderRead)
async def read_order(order_id: int, db: AsyncSession = Depends(get_db)):
    order = await get_order_by_id(db, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.delete("/{order_id}", response_model=OrderRead)
async def remove_order(order_id: int, db: AsyncSession = Depends(get_db)):
    order = await delete_order(db, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order
