from pydantic import BaseModel


class GalleryOut(BaseModel):
    id: int
    image_url: str
    category: str | None = None
    sort_order: int = 0

    class Config:
        from_attributes = True

