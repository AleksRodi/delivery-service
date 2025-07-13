from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from app.db.models.customer import Customer
from app.schemas.customer import CustomerCreate

async def get_customer_by_id(db: AsyncSession, customer_id: int):
    result = await db.execute(select(Customer).where(Customer.id == customer_id))
    return result.scalar_one_or_none()

async def list_customers_by_bot(db: AsyncSession, bot_id: int, skip: int = 0, limit: int = 100):
    result = await db.execute(
        select(Customer).where(Customer.bot_id == bot_id).offset(skip).limit(limit)
    )
    return result.scalars().all()

async def create_customer(db: AsyncSession, customer: CustomerCreate):
    db_customer = Customer(**customer.dict())
    db.add(db_customer)
    try:
        await db.commit()
        await db.refresh(db_customer)
        return db_customer
    except IntegrityError:
        await db.rollback()
        return None

async def delete_customer(db: AsyncSession, customer_id: int):
    customer = await get_customer_by_id(db, customer_id)
    if not customer:
        return None
    await db.delete(customer)
    await db.commit()
    return customer
