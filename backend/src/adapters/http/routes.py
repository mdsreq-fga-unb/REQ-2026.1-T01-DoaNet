from http.client import HTTPException
from fastapi import APIRouter, Depends
from pydantic import BaseModel  
from .security import create_access_token, verify_token

from src.domain.entities.feed_item import FeedItem
from src.adapters.http.serializers import feed_items_to_list
from src.adapters.db.mongo_feed_repository import MongoFeedRepository
from src.application.services.feed_service import FeedService

class LoginData(BaseModel):
    email: str
    password: str

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

    @router.put("/feed/{id}")
    async def update_feed(id: str, feed_item: FeedItem):
        try: 
            updated = feed_service.update_item(id, feed_item)
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
        
    @router.post("/login")
    async def login(data: LoginData):
        # 1. Valide o usuário no MongoDB aqui usando seu domain/services
        user_is_valid = (data.email == "admin@ong.org" and data.password == "123") # Simulação
    
        if not user_is_valid:
            raise HTTPException(status_code=401, detail="Credenciais incorretas")
    
    # 2. Se for válido, crie o token passando os dados que quiser (evite dados sensíveis como senha)
        token = create_access_token(data={"sub": data.email})
            
        return {"access_token": token, "token_type": "bearer"}

    return router

    
