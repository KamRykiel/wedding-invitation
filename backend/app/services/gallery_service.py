from sqlalchemy.orm import Session

from app.models import Gallery


def list_gallery(db: Session) -> list[Gallery]:
    return (
        db.query(Gallery)
        .order_by(Gallery.sort_order.asc(), Gallery.id.asc())
        .all()
    )

