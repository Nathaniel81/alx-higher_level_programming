#!/usr/bin/python3

"""Doc"""

from model_state import Base, State
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    """Doc"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
