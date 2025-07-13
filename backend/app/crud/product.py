from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from app.db.models.product import Product
from app.schemas.product import ProductCreate

async def get_product_by_id(db: AsyncSession, product_id: int):
    result = await db.execute(select(Product).where(Product.id == product_id))
    return result.scalar_one_or_none()

async def list_products_by_category(db: AsyncSession, category_id: int, skip: int = 0, limit: int = 100):
    result = await db.execute(
        select(Product).where(Product.category_id == category_id).offset(skip).limit(limit)
    )
    return result.scalars().all()

async def create_product(db: AsyncSession, product: ProductCreate):
    db_product = Product(**product.dict())
    db.add(db_product)
    try:
        await db.commit()
        await db.refresh(db_product)
        return db_product
    except IntegrityError:
        await db.rollback()
        return None

async def delete_product(db: AsyncSession, product_id: int):
    product = await get_product_by_id(db, product_id)
    if not product:
        return None
    await db.delete(product)
    await db.commit()
    return product
