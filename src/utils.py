import typing
from datetime import datetime, timedelta

import bcrypt
from jose import jwt, ExpiredSignatureError, JWTError
from pydantic import BaseModel

from src.base.config import settings
from src.exceptions import TokenExpiredException, UserNotFoundException


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str


def create_access_token(data: typing.Dict):
    return jwt.encode(data, settings.ACCESS_SECRET_KEY, algorithm=settings.ALGORITHM)

def create_refresh_token(data: typing.Dict):
    expire = datetime.utcnow() + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    return jwt.encode(data, settings.REFRESH_SECRET_KEY, algorithm=settings.ALGORITHM)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.hashpw(
        plain_password.encode('utf-8'),
        hashed_password.encode('utf-8')
    )


def refresh_access_token(refresh_token: str):
    try:
        payload = jwt.decode(refresh_token, settings.REFRESH_SECRET_KEY,algorithms=settings.ALGORITHM)

        new_access_token = create_access_token(data=dict(
            username = payload.get("username"),
            user_id = payload.get("user_id"),
            role = payload.get("role"),
            exp = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        ))

        return {
            "access_token":new_access_token,
            "refresh_token": refresh_token
        }

    except ExpiredSignatureError:
        raise TokenExpiredException
    except JWTError:
        raise  UserNotFoundException

def verify_token(token: str):
    try:
        payload = jwt.decode(
            token, settings.ACCESS_SECRET_KEY, algorithms=[settings.ALGORITHM]
        )

        return payload
    except ExpiredSignatureError:
        unverified_payload = jwt.get_unverified_claims(token)
        unverified_payload.setdefault('is_expired', True)
        return unverified_payload
    except JWTError:
        raise UserNotFoundException
