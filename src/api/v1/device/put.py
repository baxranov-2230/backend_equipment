from fastapi import Depends, APIRouter
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


from src.base.pg_db import get_db
from src.exceptions import NotDeviceException
from src.models import Device
from src.schema.devices import DevicesCreateRequest
from src.security import get_current_user, has_access

router = APIRouter( tags = ["Device"])


@router.put("/update")
@has_access(roles=['super_admin'])
async def update_device(
                            device_id: int,
                            device_data: DevicesCreateRequest,
                            db: AsyncSession = Depends(get_db),
                            current_user = Depends(get_current_user)
                        ):

    result = await db.execute(select(Device).where(Device.id == device_id))
    device = result.scalar_one_or_none()

    if device is None:
        raise NotDeviceException

    for key, value in device_data.dict(exclude_unset=True).items():
        setattr(device, key, value)

    db.add(device)
    await db.commit()
    await db.refresh(device)

    return f"Qurilamga muvvafaqiyatli ozgartirish kiritildi"