# fastapi_neon/main.py

from fastapi import FastAPI, Depends
from todofastapiapp.v1.user._user import userRouter
from todofastapiapp._database import connection_string
from sqlmodel import create_engine, SQLModel
from contextlib import asynccontextmanager
from todofastapiapp._database import create_db_and_tables


# db_engine = create_engine(
#     connection_string, connect_args={
#         "sslmode":"require"
#     },
#     pool_recycle=300
# )

# def create_db_and_tables():
#     SQLModel.metadata.create_all(db_engine)


# The first part of the function, before the yield, will
# be executed before the application starts.
# https://fastapi.tiangolo.com/advanced/events/#lifespan-function
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating tables..")
    create_db_and_tables()
    yield


app: FastAPI = FastAPI(
    lifespan=lifespan,
    title="Hello World API", 
    version="0.0.1",
    servers=[
        {
            "url": "http://0.0.0.0:8000", # ADD NGROK URL Here Before Creating GPT Action
            "description": "Development Server"
        }
    ])

#Adding routes.
app.include_router(userRouter, prefix="/user/v1", tags=["users"])

@app.get("/")
def read_root():
    return {"Hello": "World"}
