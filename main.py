from fastapi import FastAPI
from database import engine, Base
from routers import events, rsvps

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Event RSVP API")

app.include_router(events.router)
app.include_router(rsvps.router)
