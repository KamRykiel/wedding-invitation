from sqlalchemy import Boolean, DateTime, Integer, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class RSVP(Base):
    __tablename__ = "rsvp"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    attending: Mapped[bool] = mapped_column(Boolean, nullable=False)
    guests_count: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    message: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[object] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

