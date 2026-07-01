from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, Field

from domain.constants import DEFAULT_ORG_ID


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
    created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))
    org_id: Optional[str] = DEFAULT_ORG_ID