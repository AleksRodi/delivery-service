from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
from .base import Base

class DeliverySettings(Base):
    __tablename__ = "delivery_settings"
    id = Column(Integer, primary_key=True, index=True)
    bot_id = Column(Integer, ForeignKey("bots.id"), nullable=False)
    type = Column(String, nullable=False)  # delivery, pickup, etc
    params = Column(JSON, nullable=False)

    bot = relationship("Bot", back_populates="delivery_settings")
