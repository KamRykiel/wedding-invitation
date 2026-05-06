import os
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.controllers import event_router, gallery_router, messages_router, rsvp_router
from app.core.config import settings
from app.core.db import Base, SessionLocal, engine
from app.seed import seed as seed_db


def create_app() -> FastAPI:
    app = FastAPI(title="Wedding Invitation API", version="1.0.0")

    origins = [o.strip() for o in settings.cors_origins.split(",") if o.strip()]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # On Vercel serverless we generally serve images as static assets from the frontend.
    # Keep local uploads for Docker/local dev only when the directory exists.
    if os.path.isdir(settings.static_uploads_dir):
        app.mount("/static/uploads", StaticFiles(directory=settings.static_uploads_dir), name="uploads")

    @app.on_event("startup")
    def _startup():
        # Vercel/Supabase: make first deploy work without manual migrations.
        if not settings.auto_create_and_seed:
            return
        try:
            Base.metadata.create_all(bind=engine)
            db = SessionLocal()
            try:
                seed_db(db)
            finally:
                db.close()
        except Exception:
            # Don’t crash the whole app if DB isn’t configured yet.
            pass

    api = APIRouter(prefix="/api")

    @api.get("/health")
    def health():
        return {"status": "ok"}

    api.include_router(event_router)
    api.include_router(gallery_router)
    api.include_router(rsvp_router)
    api.include_router(messages_router)
    app.include_router(api)

    return app


app = create_app()

