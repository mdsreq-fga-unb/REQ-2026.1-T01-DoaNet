from datetime import datetime, timezone
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class TipoRegistro(str, Enum):
    DOACAO_EXTERNA = "doacao_externa"
    DOACAO_INTERNA = "doacao_interna"
    DESPESA = "despesa"


class TransparenciaRecord(BaseModel):
    id: Optional[str] = None
    tipo: TipoRegistro
    valor: float
    data: datetime
    descricao: str
    # Destino da doação (ex: "Projeto: X" ou "Instituição"). Só se aplica a doações.
    destino: Optional[str] = None
    created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))
    created_by: Optional[str] = None

    @field_validator("valor")
    @classmethod
    def valor_must_be_positive(cls, v: float) -> float:
        if v <= 0:
            raise ValueError("Valor deve ser maior que zero")
        return v
