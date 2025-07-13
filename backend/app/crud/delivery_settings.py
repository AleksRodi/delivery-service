from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from app.db.models.delivery_settings import DeliverySettings
from app.schemas.delivery_settings import DeliverySettingsCreate

async def get_delivery_settings_by_id(db: AsyncSession, delivery_id: int):
    result = await db.execute(select(DeliverySettings).where(DeliverySettings.id == delivery_id))
    return result.scalar_one_or_none()

async def list_delivery_settings_by_bot(db: AsyncSession, bot_id: int):
    result = await db.execute(
        select(DeliverySettings).where(DeliverySettings.bot_id == bot_id)
    )
    return result.scalars().all()

async def create_delivery_settings(db: AsyncSession, delivery: DeliverySettingsCreate):
    db_delivery = DeliverySettings(**delivery.dict())
    db.add(db_delivery)
    try:
        await db.commit()
        await db.refresh(db_delivery)
        return db_delivery
    except IntegrityError:
        await db.rollback()
        return None

async def delete_delivery_settings(db: AsyncSession, delivery_id: int):
    delivery = await get_delivery_settings_by_id(db, delivery_id)
    if not delivery:
        return None
    await db.delete(delivery)
    await db.commit()
    return delivery
