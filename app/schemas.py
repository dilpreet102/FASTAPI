from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True  #this is optional field, if user does not add this then it will take default value

class PostCreate(PostBase):
    pass


# the below class is used to display only the specific things to the user
class Post(PostBase):
    id : int
    created_at: datetime

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email : EmailStr
    password : str

class UserOut(BaseModel):
    id: int
    email : EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email : EmailStr
    password : str

class Token(BaseModel):
    access_token: str
    token_type : str

class TokenData(BaseModel):
    id: Optional[int] = None
