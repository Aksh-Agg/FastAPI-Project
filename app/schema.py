
from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional


class Post(BaseModel):
    title: str
    content: str
    published: bool= True

class usercreate(BaseModel):
    email: EmailStr
    password: str

#Response model of the schema what should it return 
class UserResponse(BaseModel):
    id: int 
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes=True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class access_token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: str

class Vote(BaseModel):
    post_id: int 
    dir: conint(ge=0, le=1)   # type: ignore