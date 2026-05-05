from typing import List

from domain.entities.feed_item import FeedItem
from domain.ports.feed_repository import FeedRepository


class FeedService:
    def __init__(self, repo: FeedRepository) -> None:
        self.repo = repo

    def list_items(self) -> List[FeedItem]:
        return self.repo.list_all()

    def add_item(self, item: FeedItem) -> None:
        self.repo.add(item)

    def delete_item(self, item_id: str) -> bool:
        return self.repo.delete(item_id)
