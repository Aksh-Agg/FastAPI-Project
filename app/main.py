from fastapi import FastAPI
# import psycopg2
# from psycopg2.extras import RealDictCursor
from app.database import  engine
import app.models as models
from app.routers import posts, users, auth, votes
from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]  

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  
    allow_headers=origins,  
)
    

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router) 