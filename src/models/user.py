from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.base.pg_db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)
    position = Column(String, nullable=False)

    devices = relationship("Device", back_populates='user')
    requests = relationship("Request", back_populates="user")
    newdevices = relationship("NewDevice", back_populates="user")

