from datetime import datetime
from typing import Optional, Any
from pydantic import BaseModel, Field, field_validator
from bson import ObjectId

class Event(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    title: str
    description: str
    date: datetime
    location: str
    max_participants: Optional[int] = None
    current_participants: int = 0
    image_url: Optional[str] = None
    created_by: str  # ID do admin que criou
    created_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = True
    
    @field_validator("id", mode="before")
    @classmethod
    def convert_objectid(cls, v: Any) -> Optional[str]:
        if isinstance(v, ObjectId):
            return str(v)
        return v
    
    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            datetime: lambda v: v.isoformat(),
            ObjectId: lambda v: str(v)
        }