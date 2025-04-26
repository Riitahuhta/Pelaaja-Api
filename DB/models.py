from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime
from typing import List



class pelaajaBase(SQLModel):
    nimi: str

class pelaaja(pelaajaBase):
    pass

class pelaajaDb(pelaajaBase, table=True):
    __tablename__ = "pelaajat"
    id: int = Field(default=None, primary_key=True)
    events: List["eventDb"] = Relationship(back_populates="pelaaja")




class eventBase(SQLModel):
    type: str
    detail: str


class event(eventBase):
    pass


class eventDb(eventBase, table=True):
    id: int = Field(default=None, primary_key=True)
    timestamp: datetime
    pelaaja: "pelaajaDb" = Relationship(back_populates="events")
    player_id: int = Field(foreign_key="pelaajat.id")


