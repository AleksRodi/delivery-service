from pydantic import BaseModel
from typing import Dict

class DeliverySettingsBase(BaseModel):
    type: str
    params: Dict

class DeliverySettingsCreate(DeliverySettingsBase):
    bot_id: int

class DeliverySettingsRead(DeliverySettingsBase):
    id: int
    bot_id: int

    class Config:
        orm_mode = True
