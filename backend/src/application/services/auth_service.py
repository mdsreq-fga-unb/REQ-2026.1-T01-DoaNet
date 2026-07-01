from typing import Optional, List
from datetime import datetime
import bcrypt
import os
from domain.ports.admin_repository import AdminRepository
from domain.entities.admin import Admin, AdminRole

class AuthService:
    def __init__(self, admin_repo: AdminRepository):
        self.admin_repo = admin_repo
    
    def hash_password(self, password: str) -> str:
        """Gera hash da senha"""
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verifica se a senha está correta"""
        return bcrypt.checkpw(
            plain_password.encode('utf-8'),
            hashed_password.encode('utf-8')
        )
    
    async def authenticate_admin(self, email: str, password: str) -> Optional[Admin]:
        """Autentica um administrador"""
        admin = await self.admin_repo.find_by_email(email)
        if not admin or not admin.is_active:
            return None
        
        if not self.verify_password(password, admin.hashed_password):
            return None
        
        # Atualiza último login
        if admin.id:
            await self.admin_repo.update_last_login(admin.id)
        
        return admin
    
    async def create_first_admin(self, email: str, name: str, password: str) -> Admin:
        """Cria o primeiro administrador (sempre será MASTER)"""
        admin_count = await self.admin_repo.count_admins()
        
        if admin_count > 0:
            raise ValueError("Já existe um administrador no sistema")
        
        hashed_password = self.hash_password(password)
        admin = Admin(
            email=email,
            name=name,
            hashed_password=hashed_password,
            role=AdminRole.MASTER,  # Primeiro admin é MASTER
            created_at=datetime.utcnow()
        )
        
        return await self.admin_repo.create(admin)
    
    async def create_admin(self, email: str, name: str, password: str, created_by: str, creator_role: str) -> Admin:
        """Cria um novo administrador (apenas MASTER pode criar)"""
        if creator_role != AdminRole.MASTER:
            raise ValueError("Apenas administradores principais podem criar novos administradores")
        
        # Verifica se email já está em uso
        existing = await self.admin_repo.find_by_email(email)
        if existing:
            raise ValueError("Email já está em uso")
        
        hashed_password = self.hash_password(password)
        admin = Admin(
            email=email,
            name=name,
            hashed_password=hashed_password,
            role=AdminRole.ADMIN,  # Novos admins são ADMIN por padrão
            created_by=created_by,
            created_at=datetime.utcnow()
        )
        
        return await self.admin_repo.create(admin)
    
    async def list_all_admins(self) -> List[Admin]:
        """Lista todos os administradores"""
        return await self.admin_repo.list_all()
    
    async def update_admin_role(self, admin_id: str, new_role: str, requester_role: str) -> bool:
        """Atualiza o papel de um admin (apenas MASTER pode fazer)"""
        if requester_role != AdminRole.MASTER:
            raise ValueError("Apenas administradores principais podem alterar papéis")
        
        return await self.admin_repo.update_role(admin_id, new_role)
    
    async def deactivate_admin(self, admin_id: str, requester_role: str) -> bool:
        """Desativa um admin (apenas MASTER pode fazer)"""
        if requester_role != AdminRole.MASTER:
            raise ValueError("Apenas administradores principais podem desativar administradores")
        
        return await self.admin_repo.deactivate_admin(admin_id)