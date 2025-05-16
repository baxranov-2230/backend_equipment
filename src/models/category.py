from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.base.pg_db import Base


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name=Column(String, nullable=False)

    devices = relationship('Device', back_populates='category')



