from app.db.session import AsyncSessionLocal
from app.db.models.bot import Bot
from app.db.models.customer import Customer
from app.db.models.category import Category
from app.db.models.product import Product
from app.db.models.order import Order
from aiogram.types import Update
import httpx
import os

TELEGRAM_API_URL = "https://api.telegram.org/bot"

async def process_update(bot_id: int, update: dict):
    # Получаем токен бота из БД
    async with AsyncSessionLocal() as db:
        bot = await db.get(Bot, bot_id)
        if not bot:
            return None

        # Пример: ответить на команду /start
        message = update.get("message")
        if message and message.get("text") == "/start":
            chat_id = message["chat"]["id"]
            await send_message(bot.telegram_token, chat_id, "Добро пожаловать!")
            # Можно добавить регистрацию клиента, показ меню и т.д.

    return None

async def send_message(token: str, chat_id: int, text: str):
    url = f"{TELEGRAM_API_URL}{token}/sendMessage"
    async with httpx.AsyncClient() as client:
        await client.post(url, json={"chat_id": chat_id, "text": text})
