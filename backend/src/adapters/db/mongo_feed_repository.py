from bson import ObjectId
from bson.errors import InvalidId

from domain.entities.feed_item import FeedItem
from domain.ports.feed_repository import FeedRepository
from adapters.db.mongo_connection import collection


class MongoFeedRepository(FeedRepository):
    def __init__(self, collection_handle=collection) -> None:
        self.collection = collection_handle

    def list_all(self):
        items = []
        for item in self.collection.find():
            items.append(
                FeedItem(
                    id=str(item["_id"]),
                    title=item.get["title"],
                    type=item.get["type"],
                    description=item.get["description"],
                    image_url=item.get["image_url"],
                    image_path=item.get["image_path"]
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