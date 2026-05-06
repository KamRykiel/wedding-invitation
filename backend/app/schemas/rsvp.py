from pydantic import BaseModel, Field


class RsvpIn(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    attending: bool
    guests_count: int = Field(ge=1, le=20)
    message: str | None = Field(default=None, max_length=2000)


class RsvpOut(BaseModel):
    id: int
    name: str
    attending: bool
    guests_count: int
    message: str | None = None

    class Config:
        from_attributes = True

