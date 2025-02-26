from jose import jwt, JWTError, ExpiredSignatureError
from jose.exceptions import JWTClaimsError
from typing import Optional
from datetime import timedelta,datetime
from passlib.context import CryptContext

from src.base.config import settings
from src.exceptions import UserNotFoundException

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# def create_access_token(data: dict) -> str:
#     return jwt.encode(data, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta if expires_delta else timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def verify_token(token: str) -> dict:

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except ExpiredSignatureError:
        raise UserNotFoundException("Token muddati tugagan, qayta login qiling")
    except JWTClaimsError:
        raise UserNotFoundException("Token noto‘g‘ri ma’lumotlarni o‘z ichiga oladi")
    except JWTError:
        raise UserNotFoundException("Token yaroqsiz yoki buzilgan")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)