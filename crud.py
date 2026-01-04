from sqlalchemy.orm import Session
from models import Event, RSVP

def create_event(db: Session, event_data: dict):
    event = Event(**event_data)
    db.add(event)
    db.commit()
    db.refresh(event)
    return event

def get_events(db: Session):
    return db.query(Event).all()

def create_rsvp(db: Session, event_id: int, name: str, email: str):
    rsvp = RSVP(name=name, email=email, event_id=event_id)
    db.add(rsvp)
    db.commit()
    db.refresh(rsvp)
    return rsvp

def get_event_rsvps(db: Session, event_id: int):
    return db.query(RSVP).filter(RSVP.event_id == event_id).all()
