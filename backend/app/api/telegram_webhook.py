from fastapi import APIRouter, Request, HTTPException, status
from app.services.telegram import process_update

router = APIRouter(tags=["telegram"])

@router.post("/telegram/webhook/{bot_id}")
async def telegram_webhook(bot_id: int, request: Request):
    update = await request.json()
    response = await process_update(bot_id, update)
    return response or {"ok": True}
