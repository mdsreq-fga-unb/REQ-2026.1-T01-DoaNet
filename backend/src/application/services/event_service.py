from typing import List, Optional
from src.domain.ports.event_repository import EventRepository
from src.domain.entities.event import Event

class EventService:
    def __init__(self, event_repo: EventRepository):
        self.event_repo = event_repo
    
    async def create_event(self, event: Event) -> Event:
        return await self.event_repo.create(event)
    
    async def list_events(self, include_inactive: bool = False) -> List[Event]:
        return await self.event_repo.list_all(include_inactive)
    
    async def get_event(self, event_id: str) -> Optional[Event]:
        return await self.event_repo.find_by_id(event_id)
    
    async def update_event(self, event_id: str, event: Event) -> bool:
        return await self.event_repo.update(event_id, event)
    
    async def delete_event(self, event_id: str) -> bool:
        return await self.event_repo.delete(event_id)
    
    async def register_participant(self, event_id: str) -> bool:
        event = await self.event_repo.find_by_id(event_id)
        if not event:
            return False
        
        if event.max_participants and event.current_participants >= event.max_participants:
            raise ValueError("Evento está lotado")
        
        return await self.event_repo.increment_participants(event_id)