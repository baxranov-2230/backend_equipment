from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class DevicesData(BaseModel):
    user_id: int
    category_id: int
    name: str
    serial_number: str
    status: str
    # created_at: Optional[datetime] = None

class DevicesCreateRequest(DevicesData):
    class Config:
        from_attributes = True


class DevicesCreateResponse(DevicesData):
    id: int

    class Config:
        from_attributes = True
