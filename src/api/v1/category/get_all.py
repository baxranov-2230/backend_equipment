from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.base.pg_db import get_db
from src.models import Device, Category
from src.security import has_access, get_current_user

router = APIRouter( tags=["Category"])


@router.get("/get")
@has_access(roles=['super_admin'])
async def get_category(current_user = Depends(get_current_user), db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(Category))
    device = result.scalars().all()

    return device

