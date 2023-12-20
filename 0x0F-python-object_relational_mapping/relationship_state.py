#!/usr/bin/python3
"""
State Module
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

m_metadata = MetaData()
Base = declarative_base(metadata=m_metadata)


class State(Base):
    """
    State class with id and name attributes
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states",
                          cascade="all, delete")
