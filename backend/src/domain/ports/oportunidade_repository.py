from abc import ABC, abstractmethod
from typing import List
from domain.entities.oportunidade import OportunidadeVoluntariado

class OportunidadeRepository(ABC):
    @abstractmethod
    def list_all(self) -> List[OportunidadeVoluntariado]:
        pass

    @abstractmethod
    def add(self, item: OportunidadeVoluntariado) -> None:
        pass

    @abstractmethod
    def update_item(self, item_id: str, item: OportunidadeVoluntariado) -> bool:
        pass

    @abstractmethod
    def delete(self, item_id: str) -> bool:
        pass