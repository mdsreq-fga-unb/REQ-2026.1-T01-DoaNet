from typing import List

from domain.entities.oportunidade import OportunidadeVoluntariado
from domain.ports.oportunidade_repository import OportunidadeRepository


class OportunidadeService:
    def __init__(self, repo: OportunidadeRepository) -> None:
        self.repo = repo

    def list_items(self) -> List[OportunidadeVoluntariado]:
        return self.repo.list_all()

    def add_item(self, item: OportunidadeVoluntariado) -> None:
        self.repo.add(item)

    def update_item(self, item_id: str, item: OportunidadeVoluntariado) -> bool:
        return self.repo.update_item(item_id, item)

    def delete_item(self, item_id: str) -> bool:
        return self.repo.delete(item_id)