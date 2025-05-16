from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.base.pg_db import get_db
from src.exceptions import NotDeviceException
from src.models import Device
from src.security import get_current_user, has_access

router = APIRouter( tags = ["Device"])


@router.delete("/delete")
@has_access(roles=['super_admin'])
async def delete_device(device_id : int, db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)):

    result = await db.execute(select(Device).where(Device.id==device_id))
    device = result.scalar_one_or_none()

    if device is None:
        raise NotDeviceException

    await db.delete(device)
    await db.commit()

    return "qurilma muvaffaqiyatli ochirildi!"