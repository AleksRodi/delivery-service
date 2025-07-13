from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from app.db.models.payment_settings import PaymentSettings
from app.schemas.payment_settings import PaymentSettingsCreate

async def get_payment_settings_by_id(db: AsyncSession, payment_id: int):
    result = await db.execute(select(PaymentSettings).where(PaymentSettings.id == payment_id))
    return result.scalar_one_or_none()

async def list_payment_settings_by_bot(db: AsyncSession, bot_id: int):
    result = await db.execute(
        select(PaymentSettings).where(PaymentSettings.bot_id == bot_id)
    )
    return result.scalars().all()

async def create_payment_settings(db: AsyncSession, payment: PaymentSettingsCreate):
    db_payment = PaymentSettings(**payment.dict())
    db.add(db_payment)
    try:
        await db.commit()
        await db.refresh(db_payment)
        return db_payment
    except IntegrityError:
        await db.rollback()
        return None

async def delete_payment_settings(db: AsyncSession, payment_id: int):
    payment = await get_payment_settings_by_id(db, payment_id)
    if not payment:
        return None
    await db.delete(payment)
    await db.commit()
    return payment
