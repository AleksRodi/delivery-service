from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from app.db.models.order import Order
from app.db.models.order_item import OrderItem
from app.schemas.order import OrderCreate

async def get_order_by_id(db: AsyncSession, order_id: int):
    result = await db.execute(select(Order).where(Order.id == order_id))
    return result.scalar_one_or_none()

async def list_orders_by_bot(db: AsyncSession, bot_id: int, skip: int = 0, limit: int = 100):
    result = await db.execute(
        select(Order).where(Order.bot_id == bot_id).offset(skip).limit(limit)
    )
    return result.scalars().all()

async def create_order(db: AsyncSession, bot_id: int, order: OrderCreate):
    db_order = Order(
        bot_id=bot_id,
        customer_id=order.customer_id,
        status="new",
        total_amount=order.total_amount,
    )
    db.add(db_order)
    await db.flush()
    item_objs = []
    for item in order.items:
        item_obj = OrderItem(
            order_id=db_order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=item.price
        )
        db.add(item_obj)
        item_objs.append(item_obj)
    try:
        await db.commit()
        await db.refresh(db_order)
        return db_order
    except IntegrityError:
        await db.rollback()
        return None

async def delete_order(db: AsyncSession, order_id: int):
    order = await get_order_by_id(db, order_id)
    if not order:
        return None
    await db.delete(order)
    await db.commit()
    return order
