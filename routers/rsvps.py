from fastapi import APIRouter, Form, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import crud, schemas

router = APIRouter(prefix="/events", tags=["RSVPs"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/{event_id}/rsvp", response_model=schemas.RSVPResponse)
def rsvp_event(
    event_id: int,
    name: str = Form(...),
    email: str = Form(...),
    db: Session = Depends(get_db)
):
    return crud.create_rsvp(db, event_id, name, email)

@router.get("/{event_id}/rsvps", response_model=list[schemas.RSVPResponse])
def get_rsvps(event_id: int, db: Session = Depends(get_db)):
    return crud.get_event_rsvps(db, event_id)
