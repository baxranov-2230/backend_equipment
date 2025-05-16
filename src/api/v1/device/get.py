from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.base.pg_db import get_db
from src.models import Device, Category, User
from src.security import has_access, get_current_user

router = APIRouter(tags=["Device"])


@router.get("/get")
@has_access(roles=['super_admin'])
async def get_device(current_user=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(
        Device.id.label('id'),
        Device.name.label('name'),
        Device.serial_number.label('serial_number'),
        Device.status.label('status'),
        Category.name.label('category_name'),
        User.full_name.label('full_name')
    ).outerjoin(Category).outerjoin(User)
                              )
    device = result.fetchall()
    return [
        dict(
            id=item.id,
            name=item.name,
            serial_number=item.serial_number,
            status=item.status,
            category_name=item.category_name,
            full_name=item.full_name
        )
        for item in device
    ]


