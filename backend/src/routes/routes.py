from fastapi import APIRouter
from models.feed_items import FeedItems
from config.database import collection_name
from schema.schemas import list_feed_items_serializer
from bson import ObjectId

router = APIRouter()

@router.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "ok"}

@router.get("/feed")
async def get_feed():
    try:
        feed_items = list_feed_items_serializer(collection_name.find())
        return feed_items
    except Exception as e:
        return {"error": str(e), "status": "failed"}
    
@router.post("/feed")
async def add_feed_item(feed_item: FeedItems):
    collection_name.insert_one(dict(feed_item))
    return {"message": "created"}

@router.delete("/feed/{id}")
async def delete_feed_item(id: str):
    try:
        result = collection_name.delete_one({"_id": ObjectId(id)})
        if result.deleted_count == 1:
            return {"message": "deleted"}
        else:
            return {"message": "item not found"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}