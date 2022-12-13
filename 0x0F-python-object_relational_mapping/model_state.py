#!/usr/bin/python3
"""Documentation"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class state(Base):
    """Doc"""
    __tablename__ = 'state'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
