from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.bot import BotRead, BotCreate
from app.crud.bot import get_bot_by_id, list_bots_by_user, create_bot, delete_bot
from app.db.session import get_db

router = APIRouter(prefix="/bots", tags=["bots"])

# Для примера user_id передаем через query (в бою — через авторизацию)
@router.post("/", response_model=BotRead, status_code=status.HTTP_201_CREATED)
async def register_bot(
    bot: BotCreate,
    user_id: int,  # В будущем брать из токена пользователя
    db: AsyncSession = Depends(get_db),
):
    created_bot = await create_bot(db, user_id, bot)
    if not created_bot:
        raise HTTPException(status_code=400, detail="Bot not created")
    return created_bot

@router.get("/", response_model=List[BotRead])
async def read_bots(
    user_id: int,  # В будущем брать из токена пользователя
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
):
    bots = await list_bots_by_user(db, user_id, skip=skip, limit=limit)
    return bots

@router.get("/{bot_id}", response_model=BotRead)
async def read_bot(bot_id: int, db: AsyncSession = Depends(get_db)):
    bot = await get_bot_by_id(db, bot_id)
    if not bot:
        raise HTTPException(status_code=404, detail="Bot not found")
    return bot

@router.delete("/{bot_id}", response_model=BotRead)
async def remove_bot(bot_id: int, db: AsyncSession = Depends(get_db)):
    bot = await delete_bot(db, bot_id)
    if not bot:
        raise HTTPException(status_code=404, detail="Bot not found")
    return bot
