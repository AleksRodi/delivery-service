from fastapi import FastAPI
from app.api import user_router, bot_router, category_router

app = FastAPI()

app.include_router(user_router)
app.include_router(bot_router)
app.include_router(category_router)

@app.get("/")
def read_root():
    return {"status": "ok"}
