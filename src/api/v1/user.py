from io import BytesIO

import pandas as pd
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy.future import select
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Query
from sqlalchemy.ext.asyncio import AsyncSession

from src.base.pg_db import get_db
from src.exceptions import NotSuperadminException, UsernameException, NotUsernameException
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

    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Login bo'lmayabti")

    access_token = create_access_token({"user": user.username, "role": user.role})
    return {"access_token": access_token, "token_type": "bearer"}



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



@user_router.post("/add_excel")
async def add_excel_user(
        file: UploadFile = File(...),
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    if current_user.role != "super_admin":
        raise NotSuperadminException

    try:
        contents = await file.read()
        excel_data = pd.read_excel(BytesIO(contents), engine="openpyxl")
    except Exception:
        raise ValueError("Faylni o‘qib bo‘lmadi.Excel fayl yuklang.")

    required_columns = {"full_name", "username", "password", "role", "position"}
    if not required_columns.issubset(excel_data.columns):
        raise ValueError("Excel faylida kerakli ustunlar yo‘q")

    users_to_add = []
    for _, row in excel_data.iterrows():
        if pd.isna(row["username"]) or pd.isna(row["password"]):
            continue

        result = await db.execute(select(User).where(User.username == row["username"]))
        existing_user = result.scalar_one_or_none()
        if existing_user:
            continue

        hashed_password = hash_password(row["password"])
        new_user = User(
            username=row["username"],
            full_name=row.get("full_name", ""),
            role=row["role"],
            position=row.get("position", ""),
            password=hashed_password,
        )

        db.add(new_user)
        users_to_add.append(new_user)

    if users_to_add:
        await db.commit()
        for user in users_to_add:
            await db.refresh(user)

    return {"message": f"{len(users_to_add)} ta foydalanuvchi qo‘shildi"}




@user_router.get("/")
async def get_user(username: str, current_user = Depends(get_current_user), db: AsyncSession = Depends(get_db)):

    if current_user.role != "super_admin":
        raise NotSuperadminException

    result = await db.execute(select(User).where(User.username==username))
    user = result.scalars().first()

    if user is None:
        raise NotUsernameException

    return user


@user_router.delete("/delete")
async def delete_user(username: str=Query(...), current_user = Depends(get_current_user), db: AsyncSession = Depends(get_db)):

    if current_user.role !="super_admin":
        raise  NotSuperadminException

    result = await  db.execute(select(User).where(User.username==username))
    user = result.scalars().first()

    if user is None:
        raise NotUsernameException

    await db.delete(user)
    await db.commit()

    return f"{username} ochirildi"