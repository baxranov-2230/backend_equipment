from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.base.pg_db import get_db
from src.models import Device, Category
from src.schema.category import CategoryCreateRequest
from src.schema.devices import DevicesCreateRequest, DevicesCreateResponse
from src.security import get_current_user, has_access

router = APIRouter( tags = ["Category"])

@router.post("/add_category")
@has_access(roles=['super_admin'])
async def add_category(
                        data_category: CategoryCreateRequest,
                        db: AsyncSession = Depends(get_db),
                        current_user = Depends(get_current_user)
                    ):

    new_category = Category(**data_category.model_dump())

    db.add(new_category)
    await db.commit()
    await db.refresh(new_category)

    return "Category muvaffaqiyatli yaratildi"
