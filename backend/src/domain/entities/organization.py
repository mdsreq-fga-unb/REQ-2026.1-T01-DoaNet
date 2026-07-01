from typing import Optional
from pydantic import BaseModel

class Organization(BaseModel):
    id: Optional[str] = None
    org_id: str
    name: str
    description: str
    primary_color: str
    background_color: str = '#FFFFFF'
    logo_url: Optional[str] = None