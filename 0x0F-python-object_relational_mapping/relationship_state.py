#!/usr/bin/python3
"""
This module contains the class definition of a State
and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    """Class with the attributes of id and namei
    for every instance of state"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(128), nullable=False,)
    cities = relationship('City', backref='states', cascade='all, delete')
