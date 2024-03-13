# fastapi_neon/main.py

from fastapi import FastAPI
from todofastapiapp.v1.user._user import userRouter

app: FastAPI = FastAPI(title="Hello World API", 
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
