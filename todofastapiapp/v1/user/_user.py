from fastapi import APIRouter
# Routes
from todofastapiapp.v1.user._read import userReadRoute

userRouter = APIRouter()

userRouter.include_router(userReadRoute, prefix="", tags=["user"])