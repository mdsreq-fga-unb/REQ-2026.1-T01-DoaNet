from datetime import datetime
from typing import Optional, Any
from pydantic import BaseModel, EmailStr, Field, field_validator
from bson import ObjectId

class Admin(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    email: EmailStr
    name: str
    hashed_password: str
    is_active: bool = True
    created_at: datetime = datetime.utcnow()
    last_login: Optional[datetime] = None
    
    @field_validator("id", mode="before")
    @classmethod
    def validate_object_id(cls, v: Any) -> Optional[str]:
        """Converte ObjectId do MongoDB para string"""
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