from typing import Annotated, Optional
from fastapi import APIRouter, File, Form, UploadFile

from domain.entities.feed_item import FeedItem
from adapters.http.serializers import feed_items_to_list
from adapters.db.mongo_feed_repository import MongoFeedRepository
from application.services.feed_service import FeedService
from adapters.infrastructure.storage.gcs_storage_service import GCSStorageService
from domain.entities.oportunidade import OportunidadeVoluntariado
from adapters.http.serializers import oportunidades_to_list
from adapters.db.mongo_oportunidade_repository import MongoOportunidadeRepository
from application.services.oportunidade_service import OportunidadeService

def innit_routes() -> APIRouter:
    router = APIRouter()

    repo = MongoFeedRepository()
    feed_service = FeedService(repo)
    storage_service = GCSStorageService(bucket_name="feed_imagens")
    oportunidade_repo = MongoOportunidadeRepository()
    oportunidade_service = OportunidadeService(oportunidade_repo)

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
        post_type: Annotated[str, Form()],
        image: Annotated[Optional[UploadFile], File()] = None,
        event_location: Annotated[Optional[str], Form()] = None,
        event_date: Annotated [Optional[str], Form()] = None,
        event_url: Annotated [Optional[str], Form()] = None
        ):

        try:
            
            if post_type == "evento":
                missing = [f for f, v in {
                    "event_location": event_location,
                    "event_date": event_date,
                    "event_url": event_url,
                }.items() if not v]
                if missing:
                    return {"error": f"Campos obrigatórios faltando: {', '.join(missing)}", "status": "failed"}

            image_data = {"image_url": None, "image_path": None}

            if image:
                image_data = storage_service.upload_image(image)

            feed_item = FeedItem(
                title = title,
                description = description,
                type = post_type,
                image_url = image_data["image_url"],
                image_path = image_data["image_path"],
                event_location = event_location if post_type == "evento" else None,
                event_date = event_date if post_type == "evento" else None,
                event_url = event_url if post_type == "evento" else None
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
        post_type: Annotated[str, Form()],
        image: Annotated [Optional[UploadFile], File()] = None,
        event_location: Annotated[Optional[str], Form()] = None,
        event_date: Annotated [Optional[str], Form()] = None,
        event_url: Annotated [Optional[str], Form()] = None
        ):

        try:

            if post_type == "evento":
                missing = [f for f, v in {
                    "event_location": event_location,
                    "event_date": event_date,
                    "event_url": event_url,
                }.items() if not v]
                if missing:
                    return {"error": f"Campos obrigatórios faltando: {', '.join(missing)}", "status": "failed"}

            current_item = feed_service.get_item(id)
            image_url = current_item.image_url
            image_path = current_item.image_path
                    
            if image:
                image_data = storage_service.upload_image(image)

                image_url = image_data["image_url"]
                image_path = image_data["image_path"]

            updated_item = FeedItem(
                title = title,
                description = description,
                type = post_type,
                image_url = image_url,
                image_path = image_path,
                event_location = event_location if post_type == "evento" else None,
                event_date = event_date if post_type == "evento" else None,
                event_url = event_url if post_type == "evento" else None
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
    
    @router.get("/oportunidades")
    async def get_oportunidades():
        try:
            items = oportunidade_service.list_items()
            return oportunidades_to_list(items)
        except Exception as exc:
            return {"error": str(exc), "status": "failed"}

    @router.post("/oportunidades")
    async def add_oportunidade(item: OportunidadeVoluntariado):
        oportunidade_service.add_item(item)
        return {"message": "created"}

    @router.put("/oportunidades/{id}")
    async def update_oportunidade(id: str, item: OportunidadeVoluntariado):
        try: 
            updated = oportunidade_service.update_item(id, item)
            if updated:
                return {"message": "updated"}
        except Exception as exc:
            return {"error": str(exc), "status": "failed"}

    @router.delete("/oportunidades/{id}")
    async def delete_oportunidade(id: str):
        try:
            deleted = oportunidade_service.delete_item(id)
            if deleted:
                return {"message": "deleted"}
            return {"message": "item not found"}
        except Exception as exc:
            return {"error": str(exc), "status": "failed"}
        
    return router