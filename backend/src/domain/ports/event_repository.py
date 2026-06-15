from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.event import Event

class EventRepository(ABC):
    @abstractmethod
    async def create(self, event: Event) -> Event:
        pass
    
    @abstractmethod
    async def find_by_id(self, event_id: str) -> Optional[Event]:
        pass
    
    @abstractmethod
    async def list_all(self, include_inactive: bool = False) -> List[Event]:
        pass
    
    @abstractmethod
    async def update(self, event_id: str, event: Event) -> bool:
        pass
    
    @abstractmethod
    async def delete(self, event_id: str) -> bool:
        pass
    
    @abstractmethod
    async def increment_participants(self, event_id: str) -> bool:
        pass