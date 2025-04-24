from fastapi import FastAPI
from contextlib import asynccontextmanager
from DB.database import create_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Käynnistetään")

    create_db()
    yield
    print("Lopetetaan")

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Hello World Hello"}