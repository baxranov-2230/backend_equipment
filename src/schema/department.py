from pydantic import BaseModel


class DepartmentData(BaseModel):
    name: str


class DepartmentRequest(DepartmentData):
    class Config:
        from_attributes = True


class DepartmentResponse:
    id: int
    class Config:
        from_attributes = True