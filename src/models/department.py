from datetime import datetime, timezone


from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from src.base.pg_db import Base


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    created_at =Column(DateTime(timezone=True), default=datetime.now(timezone.utc))

    users = relationship('User', back_populates='departments')


