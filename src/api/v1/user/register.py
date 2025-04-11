from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.base.pg_db import get_db
from src.exceptions import UsernameException
from src.models import User
from src.schema.register import RegisterUserCreateRequest

router = APIRouter()


@router.post('/register')
async def register(create_user: RegisterUserCreateRequest,
                       db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(create_user.username == User.username))
    user = result.scalars().one_or_none()
    if user:
        raise UsernameException
    new_user = User(
        full_name = create_user.full_name,
        username=create_user.username,
        password=create_user.password,
        role=create_user.role,
        contact = create_user.contact
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return {"message": "User muvaffaqiyatli yaratildi"}