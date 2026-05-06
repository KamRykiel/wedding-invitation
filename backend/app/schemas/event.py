from datetime import datetime

from pydantic import BaseModel


class EventOut(BaseModel):
    id: int
    couple_name: str
    date: datetime
    location: str
    description: str

    class Config:
        from_attributes = True

