import bcrypt
from pydantic import BaseModel, field_validator

class UserData(BaseModel):
    full_name: str
    username: str
    password: str
    role: str
    position: str

    @field_validator("password", mode="plain")
    @staticmethod
    def hash_password(value: str) -> str:
        if isinstance(value, str) and not value.startswith("$2b$"):  # Bcrypt xesh formati
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(value.encode("utf-8"), salt)
            return hashed_password.decode("utf-8")
        return value


class UserCreateRequest(UserData):
    class Config:
        from_attributes = True

class UserCreateResponse(UserData):
    id: int
    class Config:
        from_attributes = True