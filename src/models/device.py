from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.base.pg_db import Base


class Device(Base):       #Qurilma
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    model = Column(String, nullable=False)
    seria_num = Column(String(100), nullable= False)
    status = Column(String, nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates='devices')

    requests = relationship("Request", back_populates='device')