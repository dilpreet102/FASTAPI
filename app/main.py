from typing import Optional, List
from random import randrange
from fastapi import FastAPI , Response , status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
import mysql.connector
from mysql.connector import Error
from app import models, schemas, utils
from app.database import engine, get_db
from sqlalchemy.orm import Session
from app.routers import post, user, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()




# used for validating the data

try:
    connection = mysql.connector.connect(
        host = '127.0.0.1',
        database = 'fastapi',
        user = 'root',
        password = 'DilpreetAxieva123',
        autocommit = True,
        auth_plugin = 'mysql_native_password'
    )
    cur = connection.cursor(buffered=True)

    if connection.is_connected():
        print('Connected to MySQL database')

except Error as e:
    print(e)


my_posts = [{"title": "title of post1", "content": "content of post 1", "id": 1}, {"title": "title of post 2", "content": "content of post 2", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i , p in enumerate(my_posts):
        if p['id'] == id:
            return i

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)



@app.get("/")
async def root():
    return {"message": "Hello world Dilpreet Singh"}












