from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.delivery_settings import DeliverySettingsRead, DeliverySettingsCreate
from app.crud.delivery_settings import (
    get_delivery_settings_by_id,
    list_delivery_settings_by_bot,
    create_delivery_settings,
    delete_delivery_settings
)
from app.db.session import get_db

router = APIRouter(prefix="/delivery-settings", tags=["delivery-settings"])

@router.post("/", response_model=DeliverySettingsRead, status_code=status.HTTP_201_CREATED)
async def register_delivery_settings(
    delivery: DeliverySettingsCreate,
    db: AsyncSession = Depends(get_db),
):
    created_delivery = await create_delivery_settings(db, delivery)
    if not created_delivery:
        raise HTTPException(status_code=400, detail="Delivery settings not created")
    return created_delivery

@router.get("/", response_model=List[DeliverySettingsRead])
async def read_delivery_settings(
    bot_id: int,
    db: AsyncSession = Depends(get_db),
):
    delivery_settings = await list_delivery_settings_by_bot(db, bot_id)
    return delivery_settings

@router.get("/{delivery_id}", response_model=DeliverySettingsRead)
async def read_delivery_setting(delivery_id: int, db: AsyncSession = Depends(get_db)):
    delivery = await get_delivery_settings_by_id(db, delivery_id)
    if not delivery:
        raise HTTPException(status_code=404, detail="Delivery settings not found")
    return delivery

@router.delete("/{delivery_id}", response_model=DeliverySettingsRead)
async def remove_delivery_setting(delivery_id: int, db: AsyncSession = Depends(get_db)):
    delivery = await delete_delivery_settings(db, delivery_id)
    if not delivery:
        raise HTTPException(status_code=404, detail="Delivery settings not found")
    return delivery
