from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.base.pg_db import get_db
from src.models import User
from src.security import get_current_user

router = APIRouter()

@router.put('/logout')
async def logout(
        user: User = Depends(get_current_user),
        db: AsyncSession = Depends(get_db)
):

    user.is_logged_out = True
    await db.commit()
    return {"Success logout"}