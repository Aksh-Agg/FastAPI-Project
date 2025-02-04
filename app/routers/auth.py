from fastapi import APIRouter, Depends, HTTPException, Response
from..database import get_db
from sqlalchemy.orm import session
from .. import schema, models, oauth2
from passlib.context import CryptContext


pwd_context= CryptContext(schemes=["bcrypt"], deprecated= "auto")
router =APIRouter(tags=["Authentication"])

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

@router.post("/login")
async def login(user_credentials: schema.UserLogin, db: session= Depends(get_db)):
    user = db.query(models.User).filter(models.User.email== user_credentials.email).first()

    if not (user) or not (verify_password(user_credentials.password, user.password)):
        raise HTTPException(status_code=403, detail="Invalid Credentials")
    # if not verify_password(user_credentials.password, user.password):
    #     raise HTTPException(status_code=404, detail="Invalid Credentials")
    #create a token 
    # return a token
    access_token= oauth2.create_access_token(data={"user_id": user.id})
    return{"access_token": access_token}

