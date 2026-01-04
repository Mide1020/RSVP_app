from fastapi import APIRouter, Form, File, UploadFile, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import shutil, os
import crud, schemas

router = APIRouter(prefix="/events", tags=["Events"])

UPLOAD_DIR = "uploads/flyers"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.EventResponse)
def create_event(
    title: str = Form(...),
    description: str = Form(None),
    date: str = Form(...),
    location: str = Form(...),
    flyer: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    flyer_path = None
    if flyer:
        flyer_path = f"{UPLOAD_DIR}/{flyer.filename}"
        with open(flyer_path, "wb") as buffer:
            shutil.copyfileobj(flyer.file, buffer)

    event_data = {
        "title": title,
        "description": description,
        "date": date,
        "location": location,
        "flyer": flyer_path
    }

    return crud.create_event(db, event_data)

@router.get("/", response_model=list[schemas.EventResponse])
def list_events(db: Session = Depends(get_db)):
    return crud.get_events(db)
