from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.schemas import EventOut
from app.services.event_service import get_event


router = APIRouter(tags=["event"])


@router.get("/event", response_model=EventOut)
def read_event(db: Session = Depends(get_db)):
    try:
        return get_event(db)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

