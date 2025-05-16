
from fastapi import APIRouter, Depends
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.base.pg_db import get_db
from src.exceptions import  NotDepartmentException
from src.models import Department
from src.security import get_current_user, has_access

router = APIRouter ( tags=['Department'])




@router.get("/get_departments")
@has_access(roles=['super_admin'])
async def get_department(db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)):

    result = await db.execute(select(Department))
    department = result.scalars().all()

    if department is None:
        raise NotDepartmentException

    return department
