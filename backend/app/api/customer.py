from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.customer import CustomerRead, CustomerCreate
from app.crud.customer import (
    get_customer_by_id,
    list_customers_by_bot,
    create_customer,
    delete_customer
)
from app.db.session import get_db

router = APIRouter(prefix="/customers", tags=["customers"])

@router.post("/", response_model=CustomerRead, status_code=status.HTTP_201_CREATED)
async def register_customer(
    customer: CustomerCreate,
    db: AsyncSession = Depends(get_db),
):
    created_customer = await create_customer(db, customer)
    if not created_customer:
        raise HTTPException(status_code=400, detail="Customer not created")
    return created_customer

@router.get("/", response_model=List[CustomerRead])
async def read_customers(
    bot_id: int,
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
):
    customers = await list_customers_by_bot(db, bot_id, skip=skip, limit=limit)
    return customers

@router.get("/{customer_id}", response_model=CustomerRead)
async def read_customer(customer_id: int, db: AsyncSession = Depends(get_db)):
    customer = await get_customer_by_id(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.delete("/{customer_id}", response_model=CustomerRead)
async def remove_customer(customer_id: int, db: AsyncSession = Depends(get_db)):
    customer = await delete_customer(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer
