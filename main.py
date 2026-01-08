from fastapi import FastAPI
from database import engine
from models import Base
from routes import events, rsvps  # import routers

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Event RSVP System")


app.include_router(events.router)
app.include_router(rsvps.router)
