from datetime import datetime
from typing import Annotated, Optional

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from pydantic import BaseModel

from .security import (
    create_access_token,
    get_current_user_email,
    get_current_admin,
    require_master,
)

from domain.entities.feed_item import FeedItem
from domain.entities.admin import Admin, AdminRole
from domain.entities.oportunidade import OportunidadeVoluntariado

from adapters.http.serializers import feed_items_to_list, oportunidades_to_list
from adapters.db.mongo_feed_repository import MongoFeedRepository
from adapters.db.mongo_admin_repository import MongoAdminRepository
from adapters.db.mongo_oportunidade_repository import MongoOportunidadeRepository
from adapters.infrastructure.storage.gcs_storage_service import GCSStorageService

from application.services.feed_service import FeedService
from application.services.auth_service import AuthService
from application.services.oportunidade_service import OportunidadeService


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


def innit_routes() -> APIRouter:
    router = APIRouter()

    # ----- Feed e oportunidades (developer) -----
    feed_repo = MongoFeedRepository()
    feed_service = FeedService(feed_repo)
    storage_service = GCSStorageService(bucket_name="feed_imagens")
    oportunidade_repo = MongoOportunidadeRepository()
    oportunidade_service = OportunidadeService(oportunidade_repo)

    # ----- Admin / autenticação (streamlit) -----
    admin_repo = MongoAdminRepository()
    auth_service = AuthService(admin_repo)

    @router.get("/health")
    async def health():
        """Health check endpoint"""
        return {"status": "ok"}

    # ============ ROTAS DE FEED ============
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
        event_date: Annotated[Optional[str], Form()] = None,
        event_url: Annotated[Optional[str], Form()] = None
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
                title=title,
                description=description,
                type=post_type,
                image_url=image_data["image_url"],
                image_path=image_data["image_path"],
                event_location=event_location if post_type == "evento" else None,
                event_date=event_date if post_type == "evento" else None,
                event_url=event_url if post_type == "evento" else None
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
        image: Annotated[Optional[UploadFile], File()] = None,
        event_location: Annotated[Optional[str], Form()] = None,
        event_date: Annotated[Optional[str], Form()] = None,
        event_url: Annotated[Optional[str], Form()] = None
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
            if current_item is None:
                return {"error": "item not found", "status": "failed"}
            image_url = current_item.image_url
            image_path = current_item.image_path

            if image:
                image_data = storage_service.upload_image(image)
                image_url = image_data["image_url"]
                image_path = image_data["image_path"]

            updated_item = FeedItem(
                title=title,
                description=description,
                type=post_type,
                image_url=image_url,
                image_path=image_path,
                event_location=event_location if post_type == "evento" else None,
                event_date=event_date if post_type == "evento" else None,
                event_url=event_url if post_type == "evento" else None,
                created_at=current_item.created_at
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

    # ============ ROTAS DE OPORTUNIDADES ============
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

    # ============ ROTAS DE AUTENTICAÇÃO / ADMIN ============
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

        token_data = {
            "sub": admin.email,
            "admin_id": str(admin.id),
            "name": admin.name,
            "role": admin.role if admin.role else "admin"
        }

        token = create_access_token(data=token_data)

        return {
            "access_token": token,
            "token_type": "bearer",
            "admin": {
                "id": str(admin.id),
                "email": admin.email,
                "name": admin.name,
                "role": admin.role if admin.role else "admin"
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

    @router.post("/admin/create")
    async def create_admin(admin_data: CreateAdminData, current_admin: Admin = Depends(require_master)):
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

    @router.delete("/admin/{admin_id}")
    async def deactivate_admin(admin_id: str, current_admin: Admin = Depends(require_master)):
        """Desativa um administrador (apenas admin principal)"""
        if admin_id == current_admin.id:
            raise HTTPException(status_code=400, detail="Não é possível desativar a si mesmo")

        success = await auth_service.deactivate_admin(admin_id, current_admin.role)
        if not success:
            raise HTTPException(status_code=404, detail="Admin não encontrado")

        return {"message": "Administrador desativado com sucesso"}

    @router.post("/admin/register-first")
    async def register_first_admin(admin_data: CreateAdminData):
        """Registra o primeiro administrador (sempre será MASTER)"""
        try:
            admin_count = await admin_repo.count_admins()

            if admin_count > 0:
                raise HTTPException(status_code=400, detail="Já existe um administrador no sistema")

            hashed_password = auth_service.hash_password(admin_data.password)
            admin = Admin(
                email=admin_data.email,
                name=admin_data.name,
                hashed_password=hashed_password,
                role="master",
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
