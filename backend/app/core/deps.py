from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.core.jwt import decode_token
from app.crud.user import get_user_by_email

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db),
):
    token_data = decode_token(token)
    if token_data is None or token_data.email is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    user = await get_user_by_email(db, token_data.email)
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user
