from fastapi import APIRouter, Depends
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.testing.pickleable import User
from src.base.pg_db import get_db
from src.exceptions import NotSuperadminException, DepartmentException
from src.models import Department
from src.security import get_current_user

department_router = APIRouter (prefix='/department', tags=['Department'])

@department_router.post("/add_department")
async def add_department(name: str, db:AsyncSession = Depends(get_db), current_user:User =  Depends(get_current_user)):
    if current_user.role != "super_admin":
        raise NotSuperadminException

    result = await db.execute(select(Department).where(name==Department.name))
    existing_department = result.scalar_one_or_none()

    if existing_department :
        raise DepartmentException

    new_department = Department(name=name)

    db.add(new_department)
    await db.commit()
    await db.refresh(new_department)

    return new_department


@department_router.get("/")
async def get_department():
    ...

@department_router.put("/")
async def change_department():
    ...

@department_router.delete("/delete")
async def delete_department():
    ...