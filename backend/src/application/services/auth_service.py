import os
from typing import Optional
from datetime import datetime
import bcrypt
from src.domain.ports.admin_repository import AdminRepository
from src.domain.entities.admin import Admin

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
    
    async def create_admin(self, email: str, name: str, password: str, secret_key: str = None) -> Admin:
        """Cria um novo administrador"""
        # Verifica se já existe admin
        admin_count = await self.admin_repo.count_admins()
        
        # Se for o primeiro admin, não precisa de chave secreta
        # Senão, precisa da chave secreta configurada no .env
        if admin_count > 0:
            expected_secret = os.getenv("ADMIN_SECRET_KEY")
            if not secret_key or secret_key != expected_secret:
                raise ValueError("Chave secreta inválida para criar novo administrador")
        
        # Verifica se email já está em uso
        existing = await self.admin_repo.find_by_email(email)
        if existing:
            raise ValueError("Email já está em uso")
        
        # Cria o admin
        hashed_password = self.hash_password(password)
        admin = Admin(
            email=email,
            name=name,
            hashed_password=hashed_password
        )
        
        return await self.admin_repo.create(admin)