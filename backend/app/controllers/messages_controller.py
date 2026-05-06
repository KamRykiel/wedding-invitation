from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.schemas import MessageIn, MessageOut
from app.services.messages_service import create_message, list_messages


router = APIRouter(tags=["messages"])


@router.get("/messages", response_model=list[MessageOut])
def read_messages(db: Session = Depends(get_db)):
    return list_messages(db)


@router.post("/messages", response_model=MessageOut, status_code=201)
def post_message(payload: MessageIn, db: Session = Depends(get_db)):
    return create_message(db, payload)

