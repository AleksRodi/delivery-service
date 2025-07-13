import httpx
from app.db.models.bot import Bot

TELEGRAM_API_URL = "https://api.telegram.org/bot"

async def set_webhook(bot: Bot, base_webhook_url: str):
    webhook_url = f"{base_webhook_url}/telegram/webhook/{bot.id}"
    url = f"{TELEGRAM_API_URL}{bot.telegram_token}/setWebhook"
    async with httpx.AsyncClient() as client:
        resp = await client.post(url, json={"url": webhook_url})
        if resp.status_code == 200 and resp.json().get("ok"):
            bot.webhook_url = webhook_url
            bot.status = "active"
        else:
            bot.status = "error"
        return resp.json()
