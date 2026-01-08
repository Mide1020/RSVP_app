from fastapi import APIRouter, Form, File, UploadFile, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Event
from schemas import EventResponse
import os, shutil
from datetime import datetime
from typing import List

router = APIRouter(prefix="/events", tags=["Events"])

UPLOAD_DIR = "uploads/flyers"
os.makedirs(UPLOAD_DIR, exist_ok=True)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=EventResponse)
def create_event(
    title: str = Form(...),
    description: str = Form(None),
    date: str = Form(...),
    location: str = Form(...),
    flyer: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    flyer_filename = None
    if flyer:
        flyer_filename = flyer.filename
        file_path = f"{UPLOAD_DIR}/{flyer_filename}"
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(flyer.file, buffer)

    event = Event(
        title=title,
        description=description,
        date=datetime.fromisoformat(date),
        location=location,
        flyer_filename=flyer_filename
    )

    db.add(event)
    db.commit()
    db.refresh(event)
    return event

@router.get("/", response_model=List[EventResponse])
def list_events(db: Session = Depends(get_db)):
    return db.query(Event).all()
