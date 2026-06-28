from typing import List

from domain.entities.oportunidade import OportunidadeVoluntariado
from domain.ports.oportunidade_repository import OportunidadeRepository


class OportunidadeService:
    def __init__(self, repo: OportunidadeRepository) -> None:
        self.repo = repo

    def list_items(self, org_id: Optional[str] = None):
        items = self.repo.list_all()
        if org_id:
            items = [i for i in items if i.org_id == org_id]
        return items

    def add_item(self, item: OportunidadeVoluntariado) -> None:
        self.repo.add(item)

    def update_item(self, item_id: str, item: OportunidadeVoluntariado) -> bool:
        return self.repo.update_item(item_id, item)

    def delete_item(self, item_id: str) -> bool:
        return self.repo.delete(item_id)