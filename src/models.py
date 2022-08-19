import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Text, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Users(Base):
    __tablename__='users'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), nullable=False)
    firstname = Column(String(80), nullable=False)
    lastname = Column(String(80), nullable=False)
    name = Column(String(80), nullable=False)

class Comment(Base):
    __tablename__='comments'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(500))
    author_id = Column(Integer, ForeignKey("users.id"))		
    post_id = Column(Integer, ForeignKey("posts.id"))		

class Post(Base):
    __tablename__='posts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))		

class Media(Base):
    __tablename__='medias'
    id = Column(Integer, primary_key=True)
    type = Column(Integer)		
    url = Column(String(80))		
    post_id = Column(Integer, ForeignKey("posts.id"))		

class Follower(Base):
    __tablename__='followers'
    user_from_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    user_to_id = Column(Integer, ForeignKey("users.id"), primary_key=True)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')