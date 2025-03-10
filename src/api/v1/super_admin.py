from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
import os
from fastapi import APIRouter
from passlib.context import CryptContext

from src.models import User

super_admin_router = APIRouter()


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

async def create_super_admin(db: AsyncSession):

    result = await db.execute(select(User).where(User.role == "super_admin"))
    super_admin = result.scalars().first()

    if not super_admin:
        super_admin = User(
            full_name="Ahror",
            username=os.getenv('SUPER_ADMIN_USERNAME'),
            password=hash_password(os.getenv('SUPER_ADMIN_PASSWORD')),
            role='super_admin',
            contact='+998941836966'
        )
        db.add(super_admin)
        await db.commit()
        await db.refresh(super_admin)

