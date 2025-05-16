from datetime import datetime

from pydantic import BaseModel


class CategoryData(BaseModel):
    name: str


class CategoryCreateRequest(CategoryData):
    class Config:
        from_attributes = True


class CategoryCreateResponse(CategoryData):
    id: int
    class Config:
        from_attributes = True
