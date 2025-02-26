from datetime import datetime
from sqlalchemy import Integer, Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.base.pg_db import Base


class NewDevice(Base):
    __tablename__ ="newdevices"

    id =Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name_ =  Column(String, nullable=False)
    commit_ = Column(String, nullable=False)
    time = Column(DateTime, default=datetime.utcnow())

    user = relationship("User", back_populates="newdevices")