from sqlalchemy.orm import Session

from app.models import Message
from app.schemas.message import MessageIn


def list_messages(db: Session) -> list[Message]:
    return db.query(Message).order_by(Message.created_at.desc(), Message.id.desc()).all()


def create_message(db: Session, payload: MessageIn) -> Message:
    row = Message(
        content=payload.content.strip(),
        author=(payload.author.strip() if payload.author else None),
    )
    db.add(row)
    db.commit()
    db.refresh(row)
    return row

