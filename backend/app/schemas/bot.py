from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class BotBase(BaseModel):
    name: str
    telegram_token: str

class BotCreate(BotBase):
    pass

class BotRead(BotBase):
    id: int
    webhook_url: Optional[str]
    status: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True
