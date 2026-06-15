from typing import List, Optional
from src.domain.entities.feed_item import FeedItem
from src.domain.ports.feed_repository import FeedRepository

class FeedService:
    def __init__(self, repository: FeedRepository):
        self.repository = repository
    
    def list_items(self) -> List[FeedItem]:
        """Lista todos os itens do feed"""
        return self.repository.list_items()
    
    def add_item(self, item: FeedItem) -> None:
        """Adiciona um item ao feed"""
        self.repository.add_item(item)
    
    def update_item(self, item_id: str, item: FeedItem) -> bool:
        """Atualiza um item do feed"""
        return self.repository.update_item(item_id, item)
    
    def delete_item(self, item_id: str) -> bool:
        """Remove um item do feed"""
        return self.repository.delete_item(item_id)