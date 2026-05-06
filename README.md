# Wedding invitation (full-stack)

Monorepo full-stack prêt pour la prod, basé sur :
- **Frontend**: Vue 3 + Vite + Pinia (`frontend/`)
- **Backend**: FastAPI (`backend/`)
- **DB**: PostgreSQL (via Docker)
- **Images**: stockage local (`backend/app/static/uploads`) servi via `/static/uploads/*`

## Démarrage rapide (Docker)

1) Copier la config d’exemple :

```bash
cp .env.example .env
```

2) Lancer :

```bash
docker compose up --build
```

Ensuite :
- Frontend: `http://localhost:8080`
- Backend: `http://localhost:8000` (ex: `GET /api/health`)

## Dev local (sans Docker)

### Backend

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r backend/requirements.txt
export DATABASE_URL="postgresql+psycopg://postgres:postgres@localhost:5432/wedding"
alembic -c backend/alembic.ini upgrade head
python -m backend.app.seed
uvicorn backend.app.main:app --reload --port 8000
```

### Frontend

```bash
cd frontend
npm install
VITE_API_BASE_URL="http://localhost:8000" npm run dev
```

## API
- `GET /api/event`
- `GET /api/gallery`
- `POST /api/rsvp`
- `GET /api/messages`

