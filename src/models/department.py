from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.base.pg_db import Base


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    users = relationship("User", back_populates="department")  # "User" modelini chaqiramiz
