from typing import List, Optional
from bson import ObjectId
from datetime import datetime
from src.domain.ports.event_repository import EventRepository
from src.domain.entities.event import Event

class MongoEventRepository(EventRepository):
    def __init__(self, db):
        self.collection = db["events"]
    
    async def create(self, event: Event) -> Event:
        event_dict = event.dict(by_alias=True, exclude={"id"})
        result = self.collection.insert_one(event_dict)
        event.id = str(result.inserted_id)
        return event
    
    async def find_by_id(self, event_id: str) -> Optional[Event]:
        try:
            event_dict = self.collection.find_one({"_id": ObjectId(event_id)})
            if event_dict:
                if "_id" in event_dict:
                    event_dict["_id"] = str(event_dict["_id"])
                return Event(**event_dict)
        except:
            pass
        return None
    
    async def list_all(self, include_inactive: bool = False) -> List[Event]:
        query = {}
        if not include_inactive:
            query["is_active"] = True
        
        events = []
        for event_dict in self.collection.find(query).sort("date", 1):
            if "_id" in event_dict:
                event_dict["_id"] = str(event_dict["_id"])
            events.append(Event(**event_dict))
        return events
    
    async def update(self, event_id: str, event: Event) -> bool:
        try:
            event_dict = event.dict(by_alias=True, exclude={"id"})
            result = self.collection.update_one(
                {"_id": ObjectId(event_id)},
                {"$set": event_dict}
            )
            return result.modified_count > 0
        except:
            return False
    
    async def delete(self, event_id: str) -> bool:
        try:
            result = self.collection.delete_one({"_id": ObjectId(event_id)})
            return result.deleted_count > 0
        except:
            return False
    
    async def increment_participants(self, event_id: str) -> bool:
        try:
            result = self.collection.update_one(
                {"_id": ObjectId(event_id)},
                {"$inc": {"current_participants": 1}}
            )
            return result.modified_count > 0
        except:
            return False