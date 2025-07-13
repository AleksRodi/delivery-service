from pydantic import BaseModel
from typing import Dict

class PaymentSettingsBase(BaseModel):
    provider: str
    params: Dict

class PaymentSettingsCreate(PaymentSettingsBase):
    bot_id: int

class PaymentSettingsRead(PaymentSettingsBase):
    id: int
    bot_id: int

    class Config:
        orm_mode = True
