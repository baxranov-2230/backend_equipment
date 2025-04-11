from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.base.pg_db import get_db
from src.models import Device
from src.schema.devices import DevicesCreateRequest, DevicesCreateResponse
from src.security import get_current_user, has_access

router = APIRouter(prefix="/devices", tags = ["Device"])

@router.post("/add_device")
@has_access(roles=['super_admin'])
async def add_device(
                        data_device: DevicesCreateRequest,
                        db: AsyncSession = Depends(get_db),
                        current_user = Depends(get_current_user)
                    ):

    new_device = Device(**data_device.model_dump())

    db.add(new_device)
    await db.commit()
    await db.refresh(new_device)

    return DevicesCreateResponse
