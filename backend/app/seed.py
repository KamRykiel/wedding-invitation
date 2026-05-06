from __future__ import annotations

from datetime import datetime

from sqlalchemy.orm import Session

from app.core.db import SessionLocal
from app.models import Event, Gallery, Message


def seed(db: Session) -> None:
    # Event (single row)
    if not db.query(Event).first():
        db.add(
            Event(
                couple_name="Wilfried & Ornella",
                date=datetime.fromisoformat("2026-06-06T15:00:00+01:00"),
                location="Faya Hotel, Akwa — Douala, Cameroun",
                description=(
                    "C’est avec une immense joie et beaucoup d’amour que nous vous invitons "
                    "à célébrer notre union."
                ),
            )
        )

    # Gallery (static URLs served by frontend build)
    if not db.query(Gallery).first():
        db.add_all(
            [
                Gallery(image_url="/uploads/tsaf001.png", category="hero", sort_order=0),
                Gallery(image_url="/uploads/tsaf002.jpeg", category="story", sort_order=1),
                Gallery(image_url="/uploads/tsaf003.jpeg", category="story", sort_order=2),
            ]
        )

    # Quotes/messages
    if not db.query(Message).first():
        db.add_all(
            [
                Message(content="Aimer, c’est choisir chaque jour — et se retrouver, encore.", author=None),
                Message(content="La famille, c’est là où l’amour devient un foyer.", author=None),
            ]
        )

    db.commit()


def main() -> None:
    db = SessionLocal()
    try:
        seed(db)
        print("Seed completed.")
    finally:
        db.close()


if __name__ == "__main__":
    main()

