from http.client import HTTPException
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from .security import create_access_token, verify_token, get_current_user_email
from datetime import datetime
import os

from src.domain.entities.feed_item import FeedItem
from src.domain.entities.admin import Admin
from src.adapters.http.serializers import feed_items_to_list
from src.adapters.db.mongo_feed_repository import MongoFeedRepository
from src.adapters.db.mongo_admin_repository import MongoAdminRepository
from src.adapters.db.mongo_connection import db
from src.application.services.feed_service import FeedService
from src.application.services.auth_service import AuthService

class LoginData(BaseModel):
    email: str
    password: str

class AdminCreateData(BaseModel):
    email: str
    name: str
    password: str
    secret_key: str = None

def init_routes() -> APIRouter:
    router = APIRouter()
    
    # Inicializa repositórios e serviços
    feed_repo = MongoFeedRepository()
    admin_repo = MongoAdminRepository(db)
    feed_service = FeedService(feed_repo)
    auth_service = AuthService(admin_repo)
    
    @router.get("/health")
    async def health():
        """Health check endpoint"""
        return {"status": "ok"}
    
    # ============ ROTAS DE FEED ============
    @router.get("/feed")
    async def get_feed(user: str = Depends(get_current_user_email)):
        """Lista todos os itens do feed (protegido)"""
        try:
            feed_items = feed_service.list_items()
            return feed_items_to_list(feed_items)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))
    
    @router.post("/feed")
    async def add_feed_item(feed_item: FeedItem, user: str = Depends(get_current_user_email)):
        """Adiciona item ao feed (protegido)"""
        try:
            feed_service.add_item(feed_item)
            return {"message": "created"}
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))
    
    @router.put("/feed/{id}")
    async def update_feed_item(id: str, feed_item: FeedItem, user: str = Depends(get_current_user_email)):
        """Atualiza item do feed (protegido)"""
        try:
            updated = feed_service.update_item(id, feed_item)
            if updated:
                return {"message": "updated"}
            raise HTTPException(status_code=404, detail="Item not found")
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))
    
    @router.delete("/feed/{id}")
    async def delete_feed_item(id: str, user: str = Depends(get_current_user_email)):
        """Remove item do feed (protegido)"""
        try:
            deleted = feed_service.delete_item(id)
            if deleted:
                return {"message": "deleted"}
            raise HTTPException(status_code=404, detail="Item not found")
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))
    # ============ ROTAS DE AUTENTICAÇÃO ============
    @router.post("/admin/register")
    async def register_admin(admin_data: AdminCreateData):
        """Registra um novo administrador"""
        try:
            admin = await auth_service.create_admin(
                email=admin_data.email,
                name=admin_data.name,
                password=admin_data.password,
                secret_key=admin_data.secret_key
            )
            return {
                "message": "Administrador criado com sucesso",
                "admin": {
                    "id": admin.id,
                    "email": admin.email,
                    "name": admin.name
                }
            }
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro ao criar administrador: {str(e)}")
    
    @router.post("/login")
    async def login(data: LoginData):
        """Login do administrador"""
        admin = await auth_service.authenticate_admin(data.email, data.password)
        
        if not admin:
            raise HTTPException(status_code=401, detail="Credenciais incorretas")
        
        # Cria o token com os dados do admin
        token = create_access_token(data={
            "sub": admin.email,
            "admin_id": admin.id,
            "name": admin.name
        })
        
        return {
            "access_token": token,
            "token_type": "bearer",
            "admin": {
                "id": admin.id,
                "email": admin.email,
                "name": admin.name
            }
        }
    
    @router.get("/admin/verify")
    async def verify_admin_token(user_email: str = Depends(get_current_user_email)):
        """Verifica se o token é válido"""
        return {
            "valid": True,
            "email": user_email,
            "message": "Token válido"
        }
    
    @router.get("/admin/check-first")
    async def check_first_admin():
        """Verifica se já existe algum administrador cadastrado"""
        count = await admin_repo.count_admins()
        return {
            "has_admins": count > 0,
            "count": count
        }
    
    return router