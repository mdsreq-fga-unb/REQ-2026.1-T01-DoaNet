from abc import ABC, abstractmethod
from typing import Optional, List
from src.domain.entities.admin import Admin

class AdminRepository(ABC):
    @abstractmethod
    async def create(self, admin: Admin) -> Admin:
        """Cria um novo administrador"""
        pass
    
    @abstractmethod
    async def find_by_email(self, email: str) -> Optional[Admin]:
        """Busca administrador por email"""
        pass
    
    @abstractmethod
    async def find_by_id(self, admin_id: str) -> Optional[Admin]:
        """Busca administrador por ID"""
        pass
    
    @abstractmethod
    async def update_last_login(self, admin_id: str) -> None:
        """Atualiza o último login"""
        pass
    
    @abstractmethod
    async def count_admins(self) -> int:
        """Conta quantos administradores existem"""
        pass