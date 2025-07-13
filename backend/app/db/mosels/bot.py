from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base

class Bot(Base):
    __tablename__ = "bots"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String, nullable=False)
    telegram_token = Column(String, nullable=False)
    webhook_url = Column(String)
    status = Column(String, default="inactive")
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="bots")
    categories = relationship("Category", back_populates="bot")
    customers = relationship("Customer", back_populates="bot")
    orders = relationship("Order", back_populates="bot")
    payment_settings = relationship("PaymentSettings", back_populates="bot")
    delivery_settings = relationship("DeliverySettings", back_populates="bot")
