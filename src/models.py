import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(120), nullable=False, unique=True)
    following = Column(String(120)) #revisar esta relación

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    imageUrl = Column(String(250))
    caption = Column(String(250))
    comments = Column(String(250))
    likes = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)    

class Comments(Base):
    __tablename__ = 'comments'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    number_of_comments = Column(String(250))
    who_comments_id = Column(Integer, nullable=False)
    likes = Column(Integer)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

class Relationship(Base):
    __tablename__ = 'relationship'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    following_id = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')