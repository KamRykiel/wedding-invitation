from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.schemas import GalleryOut
from app.services.gallery_service import list_gallery


router = APIRouter(tags=["gallery"])


@router.get("/gallery", response_model=list[GalleryOut])
def read_gallery(db: Session = Depends(get_db)):
    return list_gallery(db)

