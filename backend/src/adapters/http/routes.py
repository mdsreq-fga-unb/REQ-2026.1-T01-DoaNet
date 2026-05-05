from fastapi import APIRouter

from domain.entities.feed_item import FeedItem
from adapters.http.serializers import feed_items_to_list
from adapters.db.mongo_feed_repository import MongoFeedRepository
from application.services.feed_service import FeedService

def innit_routes() -> APIRouter:
    router = APIRouter()

    repo = MongoFeedRepository()
    feed_service = FeedService(repo)

    @router.get("/health")
    async def health():
        """Health check endpoint."""
        return {"status": "ok"}

    @router.get("/feed")
    async def get_feed():
        try:
            feed_items = feed_service.list_items()
            return feed_items_to_list(feed_items)
        except Exception as exc:
            return {"error": str(exc), "status": "failed"}

    @router.post("/feed")
    async def add_feed_item(feed_item: FeedItem):
        feed_service.add_item(feed_item)
        return {"message": "created"}

    @router.delete("/feed/{id}")
    async def delete_feed_item(id: str):
        try:
            deleted = feed_service.delete_item(id)
            if deleted:
                return {"message": "deleted"}
            return {"message": "item not found"}
        except Exception as exc:
            return {"error": str(exc), "status": "failed"}
        
    return router

    
