from todofastapiapp import _settings
from sqlmodel import Field, Session, SQLModel, create_engine, select
from contextlib import asynccontextmanager
from fastapi import FastAPI
from todofastapiapp._settings import DATABASE_URL

connection_string = str(DATABASE_URL).replace("postgresql", "postgresql+psycopg")

# recycle connections after 5 minutes
# to correspond with the compute scale down
db_engine = create_engine(
    connection_string, connect_args={
        "sslmode":"require"
    },
    pool_recycle=300
)

def create_db_all_tables(app: FastAPI):
    SQLModel().metadata.create_all

@asynccontextmanager
async def lifespan(app:FastAPI):
    print("Creating tables...")
    create_db_all_tables(app)
    yield
    

def startSession():
    with Session(db_engine) as session:
        yield