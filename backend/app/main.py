from fastapi import FastAPI
from app.api import (
    user_router,
    bot_router,
    category_router,
    product_router,
    customer_router,
    order_router,
    payment_settings_router,
    delivery_settings_router,
)
from app.api.auth import router as auth_router
from app.api.telegram_webhook import router as telegram_webhook_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(bot_router)
app.include_router(category_router)
app.include_router(product_router)
app.include_router(customer_router)
app.include_router(order_router)
app.include_router(payment_settings_router)
app.include_router(delivery_settings_router)
app.include_router(telegram_webhook_router)

@app.get("/")
def read_root():
    return {"status": "ok"}
