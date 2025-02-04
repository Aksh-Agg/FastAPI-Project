from fastapi import FastAPI
# import psycopg2
# from psycopg2.extras import RealDictCursor
from app.database import  engine
import app.models as models
from app.routers import posts, users, auth, votes
from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]  # Define your allowed origins

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # List of HTTP methods
    allow_headers=origins,  # List of allowed headers
)
    
# try:
#     conn = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='Aksh!@#$', cursor_factory=RealDictCursor)
#     cursor= conn.cursor()
#     print("Connected to the database")
#     cursor = conn.cursor()
#     cursor.execute("SHOW port;")
#     port = cursor.fetchone()[0]
#     print(f"PostgreSQL is running on port: {port}")

# except Exception as e:
#     print(f"An error occurred: {e}")
#     conn = None


app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router) 