from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.base.pg_db import get_db
from src.models import Department

from src.security import has_access, get_current_user

router = APIRouter()


@router.get('/department_detail/{department_id}')
async def department_detail(department_id: int,
                          db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Department).where(department_id == Department.id))
    department = result.scalars().one_or_none()
    return department
