from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional

from pydantic.types import conint

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True  # this is optional field, if user does not add this then it will take default value


class PostCreate(PostBase):
    pass


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str

# the below class is used to display only the specific things to the user
class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True




class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)

