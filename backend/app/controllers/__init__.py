from app.controllers.event_controller import router as event_router
from app.controllers.gallery_controller import router as gallery_router
from app.controllers.messages_controller import router as messages_router
from app.controllers.rsvp_controller import router as rsvp_router

__all__ = ["event_router", "gallery_router", "messages_router", "rsvp_router"]

