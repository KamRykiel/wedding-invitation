from sqlalchemy.orm import Session

from app.models import Event


def get_event(db: Session) -> Event:
    event = db.query(Event).order_by(Event.id.asc()).first()
    if not event:
        raise ValueError("Event not found")
    return event

