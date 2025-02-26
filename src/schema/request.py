from pydantic import BaseModel
from sqlalchemy import DateTime


class RequestData(BaseModel):
    user_id: int
    device_id: int
    date: DateTime


class RequestCreateRequest(RequestData):
    class Config:
        from_attributes = True

class RequestCreateResponse(RequestData):
    id: int
    class Config:
        from_attributes = True
