#!/usr/bin/python3
"""
class definition of a State and an instance Base = declarative_base():
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """City class

    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The City id of the class
        name (str): The City name of the class
        state_id (int): The Foreign key
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
