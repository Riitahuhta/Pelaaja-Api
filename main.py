from fastapi import FastAPI
from contextlib import asynccontextmanager
from db.database import create_db
from routers import events, players

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Käynnistetään")

    create_db()
    yield
    print("Lopetetaan")

app = FastAPI(lifespan=lifespan)

app.include_router(players.router)
app.include_router(events.router)