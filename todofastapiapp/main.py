# fastapi_neon/main.py

from fastapi import FastAPI, Depends
from todofastapiapp.v1.user._user import userRouter
from todofastapiapp._database import connection_string, db_engine, create_db_all_tables, startSession, lifespan


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
app.include_router(userRouter, prefix="/user", tags=["users"])

@app.get("/")
def read_root():
    return {"Hello": "World"}
