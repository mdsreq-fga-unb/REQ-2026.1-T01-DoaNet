from typing import List, Protocol

from domain.entities.transparencia_record import TransparenciaRecord


class TransparenciaRepository(Protocol):
    def list_all(self) -> List[TransparenciaRecord]:
        """Retorna todos os registros ordenados por data decrescente."""
        ...

    def add(self, record: TransparenciaRecord) -> None:
        """Insere um novo registro. Registros são imutáveis após inserção."""
        ...
