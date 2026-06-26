from typing import List

from domain.entities.transparencia_record import TransparenciaRecord
from domain.ports.transparencia_repository import TransparenciaRepository


class TransparenciaService:
    def __init__(self, repo: TransparenciaRepository) -> None:
        self.repo = repo

    def list_records(self) -> List[TransparenciaRecord]:
        """Lista todos os registros. Acesso público, sem autenticação."""
        return self.repo.list_all()

    def add_record(self, record: TransparenciaRecord) -> None:
        """Adiciona novo registro de doação ou despesa."""
        self.repo.add(record)
