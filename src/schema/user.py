import bcrypt
from pydantic import BaseModel, field_validator

class UserData(BaseModel):
    department_id: int
    full_name: str
    username: str
    password: str
    role:str
    contact: str
    number_room: str



    @field_validator("password")
    def hash_password(cls, value):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(value.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')

class UserCreateRequest(UserData):
    class Config:
        from_attributes = True



class UserCreateResponse(UserData):
    id: int
    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    department_id: int
    full_name: str
    username: str
    role: str
    contact: str
    number_room: str