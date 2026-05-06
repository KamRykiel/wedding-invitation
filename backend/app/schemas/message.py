from datetime import datetime

from pydantic import BaseModel, Field


class MessageIn(BaseModel):
    content: str = Field(min_length=1, max_length=2000)
    author: str | None = Field(default=None, max_length=200)


class MessageOut(BaseModel):
    id: int
    content: str
    author: str | None = None
    created_at: datetime

    class Config:
        from_attributes = True

