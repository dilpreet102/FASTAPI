# This module is responsible for making the tables in MYSQL

from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, text, ForeignKey


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key= True, nullable=False)
    title = Column(String(250), nullable=False)
    content = Column(String(1000), nullable=False)
    published = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable = False, server_default = text('now()'))
    owner_id = Column(Integer, ForeignKey("users.id", ondelete= "CASCADE"), nullable = False)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True, nullable = False)
    email = Column(String(200) , nullable = False)
    password = Column(String(200), nullable = False)
    created_at = Column(TIMESTAMP(timezone=True), nullable = False, server_default = text('now()'))


