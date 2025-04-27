from fastapi import FastAPI
from contextlib import asynccontextmanager

from db.database import create_db
from routers import events, players
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Käynnistetään")

    create_db()
    yield
    print("Lopetetaan")

app = FastAPI(lifespan=lifespan)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(players.router)
app.include_router(events.router)