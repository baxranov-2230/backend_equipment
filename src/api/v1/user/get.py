
from sqlalchemy.future import select
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.base.pg_db import get_db
from src.exceptions import  NotUsernameException
from src.models import User

from src.security import get_current_user, has_access

router = APIRouter()






@router.get("/")
@has_access(roles=['super_admin'])
async def get_user(username: str, current_user = Depends(get_current_user), db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(User).where(User.username==username))
    user = result.scalars().first()

    if user is None:
        raise NotUsernameException

    return user