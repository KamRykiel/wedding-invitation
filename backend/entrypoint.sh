#!/usr/bin/env sh
set -e

echo "Running migrations..."
alembic -c alembic.ini upgrade head

echo "Seeding database (idempotent)..."
python -m app.seed || true

echo "Starting API..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000

