from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.base.pg_db import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String(255), nullable=False)
    category = Column(String(100), nullable=True)
    seria_number = Column(String(100), nullable=False)

    user = relationship("User", back_populates="products")