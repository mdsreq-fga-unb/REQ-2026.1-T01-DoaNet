from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class FeedItem(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    title: str
    type: str  # "post" ou "evento"
    description: str  # Note: seu repositório usa 'description', não 'content'
    image_url: Optional[str] = None
    image_path: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }