from sqlalchemy.orm import Session

from app.models import RSVP
from app.schemas.rsvp import RsvpIn


def create_rsvp(db: Session, payload: RsvpIn) -> RSVP:
    row = RSVP(
        name=payload.name.strip(),
        attending=payload.attending,
        guests_count=payload.guests_count,
        message=(payload.message.strip() if payload.message else None),
    )
    db.add(row)
    db.commit()
    db.refresh(row)
    return row

