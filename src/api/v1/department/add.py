from fastapi import APIRouter, Depends
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.testing.pickleable import User
from src.base.pg_db import get_db
from src.exceptions import DepartmentException
from src.models import Department
from src.schema.department import DepartmentRequest

from src.security import get_current_user, has_access

router = APIRouter (tags=['Department'])

@router.post("/add_department")
@has_access(roles=['super_admin'])
async def add_department(name_department: DepartmentRequest, db:AsyncSession = Depends(get_db),
                         current_user:User =  Depends(get_current_user)
                         ):
    result = await db.execute(select(Department).where(name_department.name==Department.name))
    existing_department = result.scalar_one_or_none()

    if existing_department:
        raise DepartmentException

    new_department = Department(name=name_department.name)

    db.add(new_department)
    await db.commit()
    await db.refresh(new_department)

    # print(f"Admin foydalanuvchi {current_user.username} {new_department.name} bo‘limini qoshdi")

    return new_department
