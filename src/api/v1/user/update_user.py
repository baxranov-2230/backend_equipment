from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.models import User
from src.base.pg_db import get_db
from src.exceptions import  NotDepartmentException
from src.schema.user import UserUpdate
from src.security import get_current_user, has_access

router = APIRouter()


@router.put("/update_user/{user_id}")
@has_access(roles=['super_admin'])
async def change_department(
        user_id: int,
        user_data: UserUpdate,
        current_user=Depends(get_current_user),
        db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(User).where(user_id == User.id))
    user = result.scalar_one_or_none()

    if user is None:
        raise NotDepartmentException

    user.full_name = user_data.full_name
    user.username = user_data.username
    user.role = user_data.role
    user.contact = user_data.contact
    user.number_room = user_data.number_room
    user.department_id = user_data.department_id
    await db.commit()
    await db.refresh(user)

    return f"Department '{user.full_name}' muvaffaqiyali ozgartirildi"
