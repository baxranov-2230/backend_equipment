from datetime import datetime, timedelta

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.base.config import settings
from src.base.pg_db import get_db
from src.exceptions import UserNotFoundException, CredentialsException
from src.models import User
from src.utils import verify_password, create_access_token, create_refresh_token

router = APIRouter()

@router.post('/login')
async def login_user(
        login_form: OAuth2PasswordRequestForm = Depends(),
        db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(User).where(
        login_form.username == User.username))

    user = result.scalars().one_or_none()

    if not user:
        raise UserNotFoundException

    if not verify_password(login_form.password, user.password):
        raise CredentialsException

    access_token = create_access_token(data=dict(
        username=user.username,
        user_id=user.id,
        role=user.role,
        exp=datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    ))

    refresh_token=create_refresh_token(data=dict(
        username=user.username,
        user_id=user.id,
        role=user.role,
    ))

    user.is_logged_out = False
    await db.commit()

    return {'access_token': access_token, 'refresh_token': refresh_token, "token_type": "Bearer"}