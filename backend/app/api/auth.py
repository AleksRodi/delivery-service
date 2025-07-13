from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.schemas.user import UserCreate, UserRead
from app.schemas.auth import Token, AuthDetails
from app.crud.user import get_user_by_email, create_user
from app.core.jwt import create_access_token
from app.core.security import verify_password

router = APIRouter(tags=["auth"])

@router.post("/register", response_model=UserRead)
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = await get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    created_user = await create_user(db, user)
    if not created_user:
        raise HTTPException(status_code=400, detail="User not created")
    return created_user

@router.post("/login", response_model=Token)
async def login(auth_details: AuthDetails, db: AsyncSession = Depends(get_db)):
    user = await get_user_by_email(db, auth_details.email)
    if not user or not verify_password(auth_details.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
