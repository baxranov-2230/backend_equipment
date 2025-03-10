from pydantic import BaseModel
from sqlalchemy import Column, Integer, String


class ProductData(BaseModel):
    user_id : int
    name :str
    category: str
    seria_number :str


class ProductRequest(ProductData):
    class Config:
        from_attributes = True

class ProductResponse(ProductData):
    id : int
    class Config:
        from_attributes = True