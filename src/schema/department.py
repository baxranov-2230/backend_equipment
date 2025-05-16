from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class DepartmentData(BaseModel):
    name: str
    created_at: Optional[datetime] = None


class DepartmentRequest(DepartmentData):
    class Config:
        from_attributes = True


class DepartmentResponse:
    id: int
    class Config:
        from_attributes = True