from typing import List, Optional

from domain.entities.feed_item import FeedItem
from domain.ports.feed_repository import FeedRepository


class FeedService:
    def __init__(self, repo: FeedRepository) -> None:
        self.repo = repo

    def list_items(self, org_id: Optional[str] = None):
        items = self.repo.list_all()
        if org_id:
            items = [i for i in items if i.org_id == org_id]
        return items

    def add_item(self, item: FeedItem) -> None:
        self.repo.add(item)

    def get_item(self, item_id: str) -> Optional[FeedItem]:
        return self.repo.find_by_id(item_id)

    def update_item(self, item_id: str, item: FeedItem) -> bool:
        return self.repo.update_item(item_id, item)

    def delete_item(self, item_id: str) -> bool:
        return self.repo.delete(item_id)
