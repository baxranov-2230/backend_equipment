from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.base.pg_db import get_db
from src.security import has_access, get_current_user
from src.models import User, Department

router = APIRouter()

@router.get('/get_users')
@has_access(roles=['super_admin'])
async def get_user(current_user=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    stmt = await db.execute(
        select(
            User.id.label('id'),
            User.full_name.label('full_name'),
            User.username.label('username'),
            User.role.label('role'),
            User.contact.label('contact'),
            User.number_room.label('number_room'),
            Department.name.label('department_name')
        ).outerjoin(Department)
    )
    results = stmt.fetchall()
    return [
        dict(
        id=item.id,
        full_name=item.full_name,
        username=item.username,
        role=item.role,
        contact=item.contact,
        number_room=item.number_room,
        department_name=item.department_name,
        )
        for item in results
    ]
