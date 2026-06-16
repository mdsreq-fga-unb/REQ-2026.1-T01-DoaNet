from typing import Optional

from pydantic import BaseModel


class FeedItem(BaseModel):
    id: Optional[str] = None
    title: str
    type: str
    description: str
    image_url: Optional[str] = None
    image_path: Optional[str] = None
    event_location: Optional[str] = None
    event_date: Optional[str] = None
    event_url: Optional[str] = None