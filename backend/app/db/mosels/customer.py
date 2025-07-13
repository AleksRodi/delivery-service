from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    bot_id = Column(Integer, ForeignKey("bots.id"), nullable=False)
    telegram_user_id = Column(String, nullable=False)
    name = Column(String)
    phone = Column(String)
    address = Column(String)

    bot = relationship("Bot", back_populates="customers")
    orders = relationship("Order", back_populates="customer")
