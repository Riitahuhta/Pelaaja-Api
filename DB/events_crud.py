from datetime import datetime
from fastapi import HTTPException, status
from .models import event, eventDb

events = []

event_types = {"level_started", "level_solved"}

def create_event(player_id: int, event_in: event):
    if event_in.type not in event_types:
        raise HTTPException(detail=f"Invalid event type {event_in.type}", status_code=status.HTTP_404_NOT_FOUND)
    
    new_id = len(events)
    e = eventDb(**event_in.model_dump(), player_id=player_id, id=new_id, timestamp=datetime.now())
    events.append(e.model_dump())
    return e

def get_events(event_type: str = ""):
    if event_type != "":
        if event_type not in event_types:
            raise HTTPException(detail=f"Invalid event type {event_type}", status_code=status.HTTP_404_NOT_FOUND)
        return [e for e in events if e["type"] == event_type]
    return events

def get_player_events(player_id: int, event_type: str = ""):
    if event_type != "":
        if event_type not in event_types:
            raise HTTPException(detail=f"Invalid event type {event_type}", status_code=status.HTTP_404_NOT_FOUND)
        return [e for e in events if e["player_id"] == player_id and e["type"] == event_type]
    return [e for e in events if e["player_id"] == player_id]
