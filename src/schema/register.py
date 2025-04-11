from typing import Literal

import bcrypt
from pydantic import BaseModel, field_validator


class RegisterUser(BaseModel):
    full_name: str
    username: str
    password: str
    role:  str
    contact: str

    @field_validator("password")
    def hash_password(cls, value):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(value.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')




class RegisterUserCreateRequest(RegisterUser):
    class Config:
        from_attributes = True



class RegisterUserCreateResponse(RegisterUser):
    id: int
    class Config:
        from_attributes = True