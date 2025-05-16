from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.base.pg_db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    department_id = Column(Integer, ForeignKey('departments.id'))
    full_name = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False, unique=True)
    role = Column(String, nullable=False)
    contact = Column(String, nullable=False)
    number_room = Column(String, nullable=True)


    departments = relationship('Department', back_populates='users')
    devices = relationship('Device', back_populates='users')


