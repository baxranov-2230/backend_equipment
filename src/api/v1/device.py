from fastapi import APIRouter, Depends
from mako.testing.helpers import result_lines
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.base.pg_db import get_db
from src.exceptions import NotDeviceException
from src.models import Device
from src.schema.devices import DevicesCreateRequest, DevicesCreateResponse
from src.security import get_admin_user, get_current_user

device_router = APIRouter(prefix="/devices", tags = ["Device"])

@device_router.post("/add_device")
async def add_device(
                        data_device: DevicesCreateRequest,
                        db: AsyncSession = Depends(get_db),
                        current_user = Depends(get_admin_user)
                    ):

    new_device = Device(**data_device.model_dump())

    db.add(new_device)
    await db.commit()
    await db.refresh(new_device)

    return f"{current_user} tomonidan {new_device} qoshildi"



@device_router.put("/update")
async def update_device(
                            device_id: int,
                            device_data: DevicesCreateRequest,
                            db: AsyncSession = Depends(get_db),
                            current_user = Depends(get_admin_user)
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


@device_router.get("/get")
async def get_device(current_user = Depends(get_admin_user), db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(Device))
    device = result.scalars().all()

    return device


@device_router.delete("/delete")
async def delete_device(device_id : int, db: AsyncSession = Depends(get_db), current_user = Depends(get_admin_user)):

    result = await db.execute(select(Device).where(Device.id==device_id))
    device = result.scalar_one_or_none()

    if device is None:
        raise NotDeviceException

    await db.delete(device)
    await db.commit()

    return "qurilma muvaffaqiyatli ochirildi!"