from bson import ObjectId
from typing import List, Optional
from src.domain.entities.feed_item import FeedItem
from src.domain.ports.feed_repository import FeedRepository
from src.adapters.db.mongo_connection import collection

class MongoFeedRepository(FeedRepository):
    def __init__(self, collection_handle=collection) -> None:
        self.collection = collection_handle
    
    def list_items(self) -> List[FeedItem]:
        """Lista todos os itens do feed"""
        items = []
        for item in self.collection.find().sort("created_at", -1):
            # Converte _id para id
            item_data = self._convert_item(item)
            items.append(FeedItem(**item_data))
        return items
    
    def add_item(self, item: FeedItem) -> None:
        """Adiciona um item ao feed"""
        if hasattr(item, "model_dump"):
            payload = item.model_dump()
        else:
            payload = item.dict()
        
        payload.pop("id", None)
        self.collection.insert_one(payload)
    
    def update_item(self, item_id: str, item: FeedItem) -> bool:
        """Atualiza um item do feed"""
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
    
    def delete_item(self, item_id: str) -> bool:
        """Remove um item do feed"""
        result = self.collection.delete_one({"_id": ObjectId(item_id)})
        return result.deleted_count == 1
    
    def _convert_item(self, item_dict: dict) -> dict:
        """Converte _id do MongoDB para id do Pydantic"""
        if "_id" in item_dict:
            item_dict["id"] = str(item_dict["_id"])
            del item_dict["_id"]
        return item_dict