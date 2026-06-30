from datetime import datetime
from typing import Optional, Any
from pydantic import BaseModel, EmailStr, Field, field_validator
from bson import ObjectId
from enum import Enum

class AdminRole(str, Enum):
    MASTER = "master"  # Administrador principal
    ADMIN = "admin"    # Administrador comum

class Admin(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    email: EmailStr
    name: str
    hashed_password: str
    role: AdminRole = AdminRole.ADMIN  # Por padrão é admin comum
    is_active: bool = True
    created_at: datetime = datetime.utcnow()
    created_by: Optional[str] = None  # ID do admin que criou
    last_login: Optional[datetime] = None
    org_id: Optional[str] = None
    
    @field_validator("id", mode="before")
    @classmethod
    def validate_object_id(cls, v: Any) -> Optional[str]:
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