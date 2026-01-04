from pydantic import BaseModel
from datetime import date
from typing import Optional, List

class RSVPBase(BaseModel):
    name: str
    email: str

class RSVPResponse(RSVPBase):
    id: int

    class Config:
        orm_mode = True


class EventBase(BaseModel):
    title: str
    description: Optional[str] = None
    date: date
    location: str

class EventResponse(EventBase):
    id: int
    flyer: Optional[str]
    rsvps: List[RSVPResponse] = []

    model_config = {
        "from_attributes": True
    }

