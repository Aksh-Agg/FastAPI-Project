
from fastapi import HTTPException, Depends, APIRouter
from passlib.context import CryptContext

from .. import models
from .. import schema
from..database import get_db
from sqlalchemy.orm import session

router= APIRouter(tags=["Users"])
pwd_context= CryptContext(schemes=["bcrypt"], deprecated= "auto")

@router.post("/users", status_code=201, response_model=schema.UserResponse) # status code 201 for created is passed
async def add_user(user: schema.usercreate, db: session= Depends(get_db)):
    #hashing the password before storing 
    hashed_password= pwd_context.hash(user.password)
    user.password= hashed_password
    new_user= models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/users/{id}" , response_model=schema.UserResponse)
async def get_user(id:int ,db: session= Depends(get_db)):
     user= db.query(models.User).filter(models.User.id==id).first()

     if user== None:
          raise HTTPException(status_code= 404, details= "user not found")
     return user

 