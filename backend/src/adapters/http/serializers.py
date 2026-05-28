from typing import List

from domain.entities.feed_item import FeedItem


def feed_item_to_dict(item: FeedItem) -> dict:
    if hasattr(item, "model_dump"):
        data = item.model_dump()
    else:
        data = item.dict()
    return {
        "id": data.get("id"),
        "title": data["title"],
        "type": data["type"],
        "description": data["description"],
        "image_url": data["image_url"],
        "image_path": data["image_path"]
    }


def feed_items_to_list(items: List[FeedItem]) -> list:
    return [feed_item_to_dict(item) for item in items]
