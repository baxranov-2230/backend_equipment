from io import BytesIO

import pandas as pd

from sqlalchemy.future import select
from fastapi import APIRouter, Depends, UploadFile, File, Query
from sqlalchemy.ext.asyncio import AsyncSession

from src.base.pg_db import get_db
from src.exceptions import NotSuperadminException, UsernameException
from src.models import User
from src.schema.user import UserCreateRequest
from src.security import get_current_user, has_access

router = APIRouter()



@router.post("/add")
@has_access(roles=['super_admin'])
async def add_user(
    user_data: UserCreateRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):


    result = await db.execute(select(User).where( user_data.username==User.username))
    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise UsernameException

    # hashed_password = hash_password(user_data.password)

    new_user = User(**user_data.model_dump())

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user



@router.post("/add_excel")
@has_access(roles=['super_admin'])
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

    required_columns = {"full_name", "username", "password", "role", "contact"}
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
        #
        # hashed_password = hash_password(row["password"])
        new_user = User(
            username=row["username"],
            full_name=row.get("full_name", ""),
            role=row["role"],
            contact=row.get("contact", ""),
            password = row["password"]
        )

        db.add(new_user)
        users_to_add.append(new_user)

    if users_to_add:
        await db.commit()
        for user in users_to_add:
            await db.refresh(user)

    return {"message": f"{len(users_to_add)} ta foydalanuvchi qo‘shildi"}

