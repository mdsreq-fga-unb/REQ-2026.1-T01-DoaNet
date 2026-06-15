from http.client import HTTPException
from src.application.services import auth_service
from src.application.services import event_service
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
from src.domain.entities.event import Event
from src.adapters.db.mongo_event_repository import MongoEventRepository
from src.application.services.event_service import EventService
from src.adapters.http.security import get_current_admin, require_master
from src.domain.entities.admin import AdminRole

class LoginData(BaseModel):
    email: str
    password: str

class AdminCreateData(BaseModel):
    email: str
    name: str
    password: str
    secret_key: str = None

class CreateAdminData(BaseModel):
    email: str
    name: str
    password: str

def init_routes() -> APIRouter:
    router = APIRouter()
    
    # Inicializa repositórios e serviços
    feed_repo = MongoFeedRepository()
    admin_repo = MongoAdminRepository(db)
    feed_service = FeedService(feed_repo)
    auth_service = AuthService(admin_repo)
    event_repo = MongoEventRepository(db)
    event_service = EventService(event_repo)
    
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
        
        # Debug: mostra o role no console do backend
        print(f"✅ Admin autenticado: {admin.email}")
        print(f"📋 Role do admin: {admin.role}")
        print(f"📋 Admin ID: {admin.id}")
        
        # Cria o token com os dados do admin
        token_data = {
            "sub": admin.email,
            "admin_id": str(admin.id),  # Garante que é string
            "name": admin.name,
            "role": admin.role if admin.role else "admin"  # Garante que tem um valor
        }
        
        print(f"🔑 Dados no token: {token_data}")
        
        token = create_access_token(data=token_data)
        
        # Resposta completa
        response_data = {
            "access_token": token,
            "token_type": "bearer",
            "admin": {
                "id": str(admin.id),
                "email": admin.email,
                "name": admin.name,
                "role": admin.role if admin.role else "admin"  # Garante que envia o role
            }
        }
        
        print(f"📤 Resposta enviada: {response_data}")
        
        return response_data
    
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
    
    @router.post("/admin/create")
    async def create_admin(admin_data: CreateAdminData, current_admin: Admin = Depends(require_master)):  # Apenas MASTER

      """Cria um novo administrador (apenas admin principal)"""
      try:
           new_admin = await auth_service.create_admin(
            email=admin_data.email,
            name=admin_data.name,
            password=admin_data.password,
              created_by=current_admin.id,
              creator_role=current_admin.role
        )
           return {
            "message": "Administrador criado com sucesso",
            "admin": {
                "id": new_admin.id,
                "email": new_admin.email,
                "name": new_admin.name,
                "role": new_admin.role
            }
        }
      except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
      except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    # Listar todos os admins (apenas MASTER)
    @router.get("/admin/list")
    async def list_admins(current_admin: Admin = Depends(require_master)):
        """Lista todos os administradores (apenas admin principal)"""
        admins = await auth_service.list_all_admins()
        return {
        "admins": [
            {
                "id": admin.id,
                "email": admin.email,
                "name": admin.name,
                "role": admin.role,
                "is_active": admin.is_active,
                "created_at": admin.created_at.isoformat() if admin.created_at else None
            }
            for admin in admins
        ]
    } 

    # Desativar admin (apenas MASTER)
    @router.delete("/admin/{admin_id}")
    async def deactivate_admin(
        admin_id: str,
        current_admin: Admin = Depends(require_master)
    ):
        """Desativa um administrador (apenas admin principal)"""
        if admin_id == current_admin.id:
            raise HTTPException(status_code=400, detail="Não é possível desativar a si mesmo")
        
        success = await auth_service.deactivate_admin(admin_id, current_admin.role)
        if not success:
            raise HTTPException(status_code=404, detail="Admin não encontrado")
        
        return {"message": "Administrador desativado com sucesso"}

    # ============ ROTAS DE EVENTOS ============
    @router.post("/events")
    async def create_event(
        event: Event,
        current_admin: Admin = Depends(get_current_admin)
    ):
        """Cria um novo evento (qualquer admin autenticado)"""
        try:
            event.created_by = current_admin.id
            new_event = await event_service.create_event(event)
            return {"message": "Evento criado com sucesso", "event": new_event}
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @router.get("/events")
    async def list_events(
        include_inactive: bool = False,
        current_admin: Admin = Depends(get_current_admin)
    ):
        """Lista todos os eventos"""
        try:
            events = await event_service.list_events(include_inactive)
            return {"events": [
                {
                    "id": event.id,
                    "title": event.title,
                    "description": event.description,
                    "date": event.date.isoformat(),
                    "location": event.location,
                    "max_participants": event.max_participants,
                    "current_participants": event.current_participants,
                    "image_url": event.image_url,
                    "is_active": event.is_active
                }
                for event in events
            ]}
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @router.put("/events/{event_id}")
    async def update_event(
        event_id: str,
        event: Event,
        current_admin: Admin = Depends(get_current_admin)
    ):
        """Atualiza um evento"""
        try:
            updated = await event_service.update_event(event_id, event)
            if not updated:
                raise HTTPException(status_code=404, detail="Evento não encontrado")
            return {"message": "Evento atualizado com sucesso"}
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @router.delete("/events/{event_id}")
    async def delete_event(
        event_id: str,
        current_admin: Admin = Depends(require_master)  # Apenas MASTER pode deletar
    ):
        """Remove um evento (apenas admin principal)"""
        try:
            deleted = await event_service.delete_event(event_id)
            if not deleted:
                raise HTTPException(status_code=404, detail="Evento não encontrado")
            return {"message": "Evento deletado com sucesso"}
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @router.post("/events/{event_id}/register")
    async def register_for_event(
        event_id: str,
        current_admin: Admin = Depends(get_current_admin)
    ):
        """Registra um participante no evento"""
        try:
            await event_service.register_participant(event_id)
            return {"message": "Participante registrado com sucesso"}
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))
        
    @router.post("/admin/register-first")
    async def register_first_admin(admin_data: CreateAdminData):
        """Registra o primeiro administrador (sempre será MASTER)"""
        try:
            # Verifica se já existe algum admin
            admin_count = await admin_repo.count_admins()
            
            if admin_count > 0:
                raise HTTPException(status_code=400, detail="Já existe um administrador no sistema")
            
            # Cria admin com role MASTER
            hashed_password = auth_service.hash_password(admin_data.password)
            admin = Admin(
                email=admin_data.email,
                name=admin_data.name,
                hashed_password=hashed_password,
                role="master",  # Força ser master
                is_active=True,
                created_at=datetime.utcnow()
            )
            
            created_admin = await admin_repo.create(admin)
            
            return {
                "message": "Administrador principal criado com sucesso",
                "admin": {
                    "id": created_admin.id,
                    "email": created_admin.email,
                    "name": created_admin.name,
                    "role": created_admin.role
                }
            }
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro ao criar admin: {str(e)}")  


    return router