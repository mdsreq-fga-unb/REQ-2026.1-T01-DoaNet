from abc import ABC, abstractmethod
from domain.entities.doacao import Doacao


class DoacaoRepository(ABC):
    @abstractmethod
    def save(self, doacao: Doacao) -> Doacao:
        pass

    @abstractmethod
    def update_status(self, stripe_session_id: str, status: str) -> bool:
        pass
