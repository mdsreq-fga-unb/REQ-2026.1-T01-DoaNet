from typing import List, Protocol

from domain.entities.feed_item import FeedItem


class FeedRepository(Protocol):
    def list_all(self) -> List[FeedItem]:
        ...

    def add(self, item: FeedItem) -> None:
        ...

    def update_item(self, item_id: str, item: FeedItem) -> bool:
        ...

    def delete(self, item_id: str) -> bool:
        ...
