from datetime import date
from pydantic import BaseModel, Field


class FeedItems(BaseModel):
    title: str
    type: str
    description: str
   
