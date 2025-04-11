from datetime import datetime

from pydantic import BaseModel


class DepartmentData(BaseModel):
    name: str
    created_at: datetime


class DepartmentRequest(DepartmentData):
    class Config:
        from_attributes = True


class DepartmentResponse:
    id: int
    class Config:
        from_attributes = True