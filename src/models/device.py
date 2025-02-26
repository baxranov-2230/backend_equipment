from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.base.pg_db import Base


class Device(Base):       #Qurilma
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False) # Qurilmaning nomi
    model = Column(String, nullable=False)   #Qurilma modeli
    seria_num = Column(String(100), nullable= False) #seriya nomeri
    status = Column(String, nullable=False)  #Qurilma holati

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates='devices')

    requests = relationship("Request", back_populates='device')