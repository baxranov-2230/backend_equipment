from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.testing.pickleable import User
from src.base.pg_db import get_db
from src.exceptions import DepartmentException, NotDepartmentException
from src.models import Department
from src.schema.department import DepartmentRequest
from src.security import get_current_user, has_access

router = APIRouter (tags=['Department'])
@router.put("/update_department/{department_id}")
@has_access(roles=['super_admin'])
async def change_department(
                                department_id: int,
                                department_data: DepartmentRequest,
                                current_user = Depends(get_current_user),
                                db: AsyncSession=Depends(get_db)
                            ):

    result = await db.execute(select(Department).where(department_id==Department.id))
    department =result.scalar_one_or_none()

    if department is None:
        raise NotDepartmentException

    for key, value in department_data.dict(exclude_unset=True).items():
        if isinstance(value, datetime) and value.tzinfo:
            value = value.replace(tzinfo=None)
        setattr(department, key, value)
    db.add(department)
    await db.commit()
    await db.refresh(department)

    return f"Department '{department.name}' muvaffaqiyali ozgartirildi"