from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
from .base import Base

class PaymentSettings(Base):
    __tablename__ = "payment_settings"
    id = Column(Integer, primary_key=True, index=True)
    bot_id = Column(Integer, ForeignKey("bots.id"), nullable=False)
    provider = Column(String, nullable=False)
    params = Column(JSON, nullable=False)

    bot = relationship("Bot", back_populates="payment_settings")
