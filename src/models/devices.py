from datetime import datetime, timezone

from sqlalchemy import Column, Integer, String, ForeignKey, func, TIMESTAMP, DateTime
from sqlalchemy.orm import relationship

from src.base.pg_db import Base


class Device(Base):
    __tablename__ = 'devices'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))
    name = Column(String, nullable=False)
    serial_number = Column(String, nullable=False)
    status = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.now(timezone.utc))

    users = relationship('User', back_populates='devices')
    category = relationship('Category', back_populates='devices')