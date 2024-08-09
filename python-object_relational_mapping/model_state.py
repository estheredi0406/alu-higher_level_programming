#!/usr/bin/python3
"""
This module defines the State model, which is used to represent a state in a MySQL database.

The State model inherits from SQLAlchemy's Base and links to the MySQL table 'states'.
It includes the following attributes:
- id: An integer that serves as the primary key.
- name: A string representing the name of the state.

The module uses SQLAlchemy's ORM to map the State class to the 'states' table in the database.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a state for a MySQL database.

    __tablename__ (str): The name of the MySQL table to store States.
    id (sqlalchemy.Integer): The state's id.
    name (sqlalchemy.String): The state's name.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
