from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class EventBase(BaseModel):
    title: str
    description: Optional[str] = None
    date: datetime
    location: str
    flyer_filename: Optional[str] = None

class EventResponse(EventBase):
    id: int

    model_config = {
        "from_attributes": True  
    }

class RSVPBase(BaseModel):
    name: str
    email: str

class RSVPResponse(RSVPBase):
    id: int
    event_id: int

    model_config = {
        "from_attributes": True
    }
