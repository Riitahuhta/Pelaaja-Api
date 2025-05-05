from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from db.database import get_session
from db.models import pelaaja, pelaajaDb
from db import players_crud

router = APIRouter(prefix="/players", tags=["players"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_players(player: pelaaja, session: Session = Depends(get_session)):
    return players_crud.create_players(session, player)

@router.get("/", response_model=list[pelaajaDb])
def get_players(players: str = "", session: Session = Depends(get_session)):
    return players_crud.get_players(session, players)

@router.get("/{player_id}", response_model=pelaajaDb)
def get_player_by_id(player_id: int, session: Session = Depends(get_session)):
    return players_crud.get_player_by_id(session, player_id)

@router.delete("/{player_id}")
def delete_player(player_id: int, session: Session = Depends(get_session)):
    return players_crud.delete_player(session, player_id)