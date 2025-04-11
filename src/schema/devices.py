from datetime import datetime

from pydantic import BaseModel


class DevicesData(BaseModel):
    user_id: int
    name: str
    serial_number: str
    status: str
    created_at: datetime

class DevicesCreateRequest(DevicesData):
    class Config:
        from_attributes = True


class DevicesCreateResponse(DevicesData):
    id: int

    class Config:
        from_attributes = True
