"""init

Revision ID: 0001_init
Revises: 
Create Date: 2026-05-06

"""

from __future__ import annotations

from alembic import op
import sqlalchemy as sa


revision = "0001_init"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "event",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("couple_name", sa.Text(), nullable=False),
        sa.Column("date", sa.DateTime(timezone=True), nullable=False),
        sa.Column("location", sa.Text(), nullable=False),
        sa.Column("description", sa.Text(), nullable=False, server_default=""),
    )

    op.create_table(
        "gallery",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("image_url", sa.Text(), nullable=False),
        sa.Column("category", sa.Text(), nullable=True),
        sa.Column("sort_order", sa.Integer(), nullable=False, server_default="0"),
    )

    op.create_table(
        "rsvp",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.Text(), nullable=False),
        sa.Column("attending", sa.Boolean(), nullable=False),
        sa.Column("guests_count", sa.Integer(), nullable=False, server_default="1"),
        sa.Column("message", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
    )

    op.create_table(
        "messages",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("author", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("messages")
    op.drop_table("rsvp")
    op.drop_table("gallery")
    op.drop_table("event")

