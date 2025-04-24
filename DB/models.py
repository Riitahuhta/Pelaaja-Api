from typing import List
from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime



class pelaajaBase(SQLModel):
    nimi: str

class pelaaja(pelaajaBase):
    id: int

class pelaajaDb(pelaajaBase, table=True):
    id: int = Field(default=None, primary_key=True)
    events: "eventDb" = Relationship(back_populates="pelaaja")



class eventBase(SQLModel):
    type: str
    detail: str

class event(eventBase):
    id: int
    timestamp: datetime
    pelaaja_id: int

class eventDb(eventBase, table=True):
    id: int = Field(default=None, primary_key=True)
    player_id: int = Field(foreign_key="pelaaja.id")
    pelaaja: "pelaajaDb" = Relationship(back_populates="events")
