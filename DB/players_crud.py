from fastapi import HTTPException, status
from .models import pelaaja, pelaajaDb
from sqlmodel import Session, select

def create_players(session: Session, player: pelaaja):
    p = pelaajaDb.model_validate(player)
    session.add(p)
    session.commit()
    session.refresh(p)
    return p

def get_players(session: Session, nimi: str = ""):
    if nimi != "":
        return session.exec(select(pelaajaDb).where(pelaajaDb.nimi == nimi)).all()
    return session.exec(select(pelaajaDb)).all()

def get_player_by_id(session: Session, player_id: int):
    p = session.get(pelaajaDb, player_id)
    if not p:
        raise HTTPException(detail="Player not found", status_code=status.HTTP_404_NOT_FOUND)
    return p

def delete_player(session: Session, player_id: int):
    p = session.get(pelaajaDb, player_id)
    if not p:
        raise HTTPException(detail="Player not found", status_code=status.HTTP_404_NOT_FOUND)
    session.delete(p)
    session.commit()
    return{"message": "Player {player_id} deleted"}