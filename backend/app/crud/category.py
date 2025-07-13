from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from app.db.models.category import Category
from app.schemas.category import CategoryCreate

async def get_category_by_id(db: AsyncSession, category_id: int):
    result = await db.execute(select(Category).where(Category.id == category_id))
    return result.scalar_one_or_none()

async def list_categories_by_bot(db: AsyncSession, bot_id: int, skip: int = 0, limit: int = 100):
    result = await db.execute(
        select(Category).where(Category.bot_id == bot_id).offset(skip).limit(limit)
    )
    return result.scalars().all()

async def create_category(db: AsyncSession, bot_id: int, category: CategoryCreate):
    db_category = Category(
        bot_id=bot_id,
        name=category.name,
        sort_order=category.sort_order or 0
    )
    db.add(db_category)
    try:
        await db.commit()
        await db.refresh(db_category)
        return db_category
    except IntegrityError:
        await db.rollback()
        return None

async def delete_category(db: AsyncSession, category_id: int):
    category = await get_category_by_id(db, category_id)
    if not category:
        return None
    await db.delete(category)
    await db.commit()
    return category
