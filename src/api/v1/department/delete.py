
from fastapi import APIRouter, Depends
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.base.pg_db import get_db
from src.exceptions import NotDepartmentException
from src.models import Department
from src.security import get_current_user, has_access

router = APIRouter ( tags=['Department'])



@router.delete("/delete_department/{department_id}")
@has_access(roles=['super_admin'])
async def delete_department(department_id: int, current_user = Depends(get_current_user),
                            db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(Department).where(department_id==Department.id))
    department = result.scalar_one_or_none()

    if department is None:
        raise  NotDepartmentException

    await db.delete(department)
    await db.commit()

    print(f"Admin foydalanuvchi {current_user.username} {department.name} bo‘limini ochirdi")


    return "muvafaqqiyatli ochirildi"