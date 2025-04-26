from fastapi import APIRouter, status
from db.models import event, eventDb
from db import events_crud

router = APIRouter(prefix="/events", tags=["events"])

@router.post("/{player_id}", response_model=event, status_code=status.HTTP_201_CREATED)
def create_event_for_player(player_id: int, event_in: event):
    return events_crud.create_event(player_id, event_in)

@router.get("/", response_model=list[eventDb])
def list_events(event_type: str = ""):
    return events_crud.get_events(event_type)

@router.get("/{player_id}", response_model=list[eventDb])
def list_player_events(player_id: int, event_type: str = ""):
    return events_crud.get_player_events(player_id, event_type)