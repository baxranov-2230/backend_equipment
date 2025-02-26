import typing
from functools import wraps

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.base.pg_db import get_db
from src.exceptions import CredentialsException, InvalidRoleException, SecurityException
from src.models import User
from src.utils import verify_token

security_schema = OAuth2PasswordBearer(tokenUrl="/v1/users/login")

async def get_current_user(
        token: str = Depends(security_schema), db: AsyncSession = Depends(get_db)
):
    payload = verify_token(token)


    if not payload or "user" not in payload:
        raise CredentialsException("Invalid token")

    username: str = payload.get("user")

    result = await db.execute(select(User).where(User.username == username))
    user = result.scalar_one_or_none()

    if user is None:
        raise CredentialsException("User not found")
    return user


def has_access(roles: typing.List[str]):
    def decorator(func):
        @wraps(func)
        async def wrapper(current_user: User = Depends(get_current_user), *args, **kwargs):
            if current_user.role not in roles:
                raise InvalidRoleException

            return await func(*args, **kwargs)

        return wrapper

    return decorator


async def get_admin_user(user: User = Depends(get_current_user)):
    if user.role != "super_admin":
        raise InvalidRoleException("Only super admin can access this")
    return user

