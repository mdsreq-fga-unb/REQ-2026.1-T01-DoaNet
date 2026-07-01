from abc import ABC, abstractmethod
from typing import Optional
from domain.entities.doacao import Doacao


class DoacaoRepository(ABC):
    @abstractmethod
    def save(self, doacao: Doacao) -> Doacao:
        pass

    @abstractmethod
    def update_status(self, stripe_session_id: str, status: str) -> bool:
        pass

    @abstractmethod
    def find_by_session_id(self, stripe_session_id: str) -> Optional[Doacao]:
        pass

    @abstractmethod
    def update_by_session_id(self, stripe_session_id: str, campos: dict) -> bool:
        pass
