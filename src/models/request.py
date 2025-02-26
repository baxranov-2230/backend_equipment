from datetime import datetime
from sqlalchemy import Column,String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from src.base.pg_db import Base


class Request(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates="requests")

    device_id = Column(Integer, ForeignKey('devices.id'))
    device = relationship('Device', back_populates='requests')

    date = Column(DateTime, default=datetime.utcnow())
    commit = Column(String, nullable=True)