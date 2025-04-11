import typing
from functools import wraps

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from mako.testing.helpers import result_lines
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.base.pg_db import get_db
from src.exceptions import CredentialsException, InvalidRoleException, SecurityException, UserNotFoundException, \
    NotSuperadminException, TokenExpiredException, UserLoggedOutException
from src.models import User
from src.utils import verify_token

security_schema = OAuth2PasswordBearer(tokenUrl="/v1/user/login")


async def get_current_user(
        token: str = Depends(security_schema), db: AsyncSession = Depends(get_db)
):
    paylaod = verify_token(token)

    username: str = paylaod.get("username")

    if username is None:
        raise CredentialsException

    result = await db.execute(select(User).filter(username==User.username))
    user: User = result.scalars().first()

    if 'is_expired' in paylaod:
        user.is_logged_out = True
        await db.commit()
        raise TokenExpiredException

    if user is None:
        raise CredentialsException



    return user


def has_access(roles: typing.List[str]):
    def decorator(func):
        @wraps(func)
        async def wrapper (*args, **kwargs):
            user = kwargs.get('current_user')
            if user.role not in roles:
                raise InvalidRoleException
            result = await func(*args, **kwargs)
            return result
        return wrapper
    return decorator