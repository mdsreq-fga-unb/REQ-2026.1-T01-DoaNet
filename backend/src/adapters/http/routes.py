from typing import Annotated, Optional
from fastapi import APIRouter, File, Form, UploadFile

from domain.entities.feed_item import FeedItem
from adapters.http.serializers import feed_items_to_list
from adapters.db.mongo_feed_repository import MongoFeedRepository
from application.services.feed_service import FeedService
from infrastructure.storage.gcs_storage_service import GCSStorageService

def innit_routes() -> APIRouter:
    router = APIRouter()

    repo = MongoFeedRepository()
    feed_service = FeedService(repo)
    storage_service = GCSStorageService(bucket_name="feed_imagens")

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
    async def add_feed_item(
        title: Annotated[str, Form()],
        description: Annotated[str, Form()],
        image: Annotated[Optional[UploadFile], File()] = None
        ):
        
        try:
            image_data = {"image_url": None, "imagem_path": None}

            if image:
                image_data = storage_service.upload_image(image)

            feed_item = FeedItem(
                title = title,
                description = description,
                image_url = image_data["image_url"],
                image_path = image_data["image_path"]
            )

            feed_service.add_item(feed_item)
            return {"message": "created"}
        except Exception as exc:
            return {"error": str(exc), "status": "failed"}

    @router.put("/feed/{id}")
    async def update_feed(
        id: str, 
        title: Annotated[str, Form()],
        description: Annotated[str, Form()],
        image: Annotated [Optional[UploadFile], File()] = None
        ):

        try:
            if image:
                image_data = storage_service.upload_image(image)

                image_url = image_data["image_url"]
                image_path = image_data["image_path"]

            updated_item = FeedItem(
                title = title,
                description = description,
                image_url = image_url,
                image_path = image_path
            )

            updated = feed_service.update_item(id, updated_item)
            if updated:
                return {"message": "updated"}

        except Exception as exc:
            return {"error": str(exc), "status": "failed"}

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