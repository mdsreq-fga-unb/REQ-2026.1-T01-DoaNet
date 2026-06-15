from typing import List
from src.domain.entities.feed_item import FeedItem

def feed_items_to_list(items: List[FeedItem]) -> List[dict]:
    """Converte lista de FeedItem para lista de dicionários"""
    return [
        {
            "id": item.id,
            "title": item.title,
            "type": item.type,
            "description": item.description,
            "created_at": item.created_at.isoformat() if item.created_at else None
        }
        for item in items
    ]