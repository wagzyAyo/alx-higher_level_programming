#!/usr/bin/python3
"""
This module contains the class definition of a State
and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

my_meta = MetaData()
Base = declarative_base(metadata=my_meta)

class State(Base):
    """Class with the attributes of id and name
    for every instance of state"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False,)
