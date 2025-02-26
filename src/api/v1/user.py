from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy.future import select
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.base.pg_db import get_db
from src.exceptions import NotSuperadminException, UsernameException
from src.models import User
from src.schema.user import UserCreateRequest
from src.security import get_current_user
from src.utils import verify_password, create_access_token, hash_password

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


user_router = APIRouter(prefix='/users',tags=["User"])

@user_router.post("/login", response_model=TokenResponse)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(User).where(User.username == form_data.username))
    user = result.scalars().first()

    if not user or verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Login bo'lmayabti")

    access_token = create_access_token({"user": user.username, "role": user.role})
    return {"access_token": access_token, "token_type": "bearer"}

@user_router.post()

@user_router.post("/add")
async def add_user(
    user_data: UserCreateRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    if current_user.role != "super_admin":
        raise NotSuperadminException

    result = await db.execute(select(User).where(User.username == user_data.username))
    existing_user = result.scalar_one_or_none()
    if existing_user:
        raise UsernameException

    hashed_password = hash_password(user_data.password)

    new_user = User(**user_data.model_dump(exclude={"password"}))
    new_user.password = hashed_password
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user
