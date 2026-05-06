from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.schemas import RsvpIn, RsvpOut
from app.services.rsvp_service import create_rsvp


router = APIRouter(tags=["rsvp"])


@router.post("/rsvp", response_model=RsvpOut, status_code=201)
def post_rsvp(payload: RsvpIn, db: Session = Depends(get_db)):
    return create_rsvp(db, payload)

