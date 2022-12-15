#!/usr/bin/python3

"""Doc"""

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base


class City(Base):
    """Doc"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
