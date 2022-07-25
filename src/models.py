import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Users(Base):
    __tablename__='Users'
    id = Column(Integer, primary_key=True)
    email = Column(String(80), nullable=False)
    password = Column(String(80), nullable=False)
    name = Column(String(80))
    lastname = Column(String(80))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')