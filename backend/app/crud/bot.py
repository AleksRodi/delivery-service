from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from app.db.models.bot import Bot
from app.schemas.bot import BotCreate
from app.services.bot_webhook import set_webhook

async def get_bot_by_id(db: AsyncSession, bot_id: int):
    result = await db.execute(select(Bot).where(Bot.id == bot_id))
    return result.scalar_one_or_none()

async def list_bots_by_user(db: AsyncSession, user_id: int, skip: int = 0, limit: int = 100):
    result = await db.execute(
        select(Bot).where(Bot.user_id == user_id).offset(skip).limit(limit)
    )
    return result.scalars().all()

async def create_bot(db: AsyncSession, user_id: int, bot: BotCreate):
    db_bot = Bot(
        user_id=user_id,
        name=bot.name,
        telegram_token=bot.telegram_token,
        webhook_url=None,
        status="inactive"
    )
    db.add(db_bot)
    try:
        await db.commit()
        await db.refresh(db_bot)
        return db_bot
    except IntegrityError:
        await db.rollback()
        return None

async def delete_bot(db: AsyncSession, bot_id: int):
    bot = await get_bot_by_id(db, bot_id)
    if not bot:
        return None
    await db.delete(bot)
    await db.commit()
    return bot

async def create_bot(db: AsyncSession, user_id: int, bot: BotCreate, base_webhook_url: str):
    db_bot = Bot(
        user_id=user_id,
        name=bot.name,
        telegram_token=bot.telegram_token,
        webhook_url=None,
        status="inactive"
    )
    db.add(db_bot)
    try:
        await db.commit()
        await db.refresh(db_bot)
        await set_webhook(db_bot, base_webhook_url)
        await db.commit()
        await db.refresh(db_bot)
        return db_bot
    except IntegrityError:
        await db.rollback()
        return None
