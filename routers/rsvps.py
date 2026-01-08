from fastapi import APIRouter, Form, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import RSVP
from schemas import RSVPResponse
from typing import List

router = APIRouter(prefix="/events", tags=["RSVPs"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/{event_id}/rsvp", response_model=RSVPResponse)
def rsvp_event(
    event_id: int,
    name: str = Form(...),
    email: str = Form(...),
    db: Session = Depends(get_db)
):
    rsvp = RSVP(name=name, email=email, event_id=event_id)
    db.add(rsvp)
    db.commit()
    db.refresh(rsvp)
    return rsvp

@router.get("/{event_id}/rsvps", response_model=List[RSVPResponse])
def get_rsvps(event_id: int, db: Session = Depends(get_db)):
    return db.query(RSVP).filter(RSVP.event_id == event_id).all()
