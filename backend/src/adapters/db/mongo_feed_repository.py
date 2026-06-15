from bson import ObjectId
from bson.errors import InvalidId

from domain.entities.feed_item import FeedItem
from domain.ports.feed_repository import FeedRepository
from adapters.db.mongo_connection import get_collection


class MongoFeedRepository(FeedRepository):
    def __init__(self, collection_handle=None) -> None:
        self.collection = collection_handle or get_collection()

    def list_all(self):
        items = []
        for item in self.collection.find():
            items.append
            (
                FeedItem(
                    id=str(item["_id"]),
                    title=item.get("title"),
                    type=item.get("type"),
                    description=item.get("description"),
                    image_url=item.get("image_url"),
                    image_path=item.get("image_path"),
                    event_location=item.get("event_location"),
                    event_date=item.get("event_date"),
                    event_url=item.get("event_url")
                )
            )
        return items

    def add(self, item: FeedItem) -> None:
        if hasattr(item, "model_dump"):
            payload = item.model_dump()
        else:
            payload = item.dict()
        payload.pop("id", None)
        self.collection.insert_one(payload)

    def update_item(self, item_id: str, item: FeedItem) -> bool:
        if not ObjectId.is_valid(item_id):
            return False

        if hasattr(item, "model_dump"):
            payload = item.model_dump()
        else:
            payload = item.dict()

        payload.pop("id", None)
        result = self.collection.update_one(
            {"_id": ObjectId(item_id)},
            {"$set": payload}
        )
        return result.matched_count == 1

    def delete(self, item_id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(item_id)})
        return result.deleted_count == 1