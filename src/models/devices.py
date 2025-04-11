from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey,func, TIMESTAMP
from sqlalchemy.orm import relationship

from src.base.pg_db import Base


class Device(Base):
    __tablename__ = 'devices'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String, nullable=False)
    serial_number = Column(String, nullable=False)
    status = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

    users = relationship('User', back_populates='devices')