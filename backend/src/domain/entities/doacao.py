from typing import Optional
from pydantic import BaseModel


class Doacao(BaseModel):
    id: Optional[str] = None
    valor: float
    is_anonima: bool
    nome_doador: Optional[str] = None
    direcao: str  # "instituicao" | "projeto"
    nome_projeto: Optional[str] = None
    stripe_session_id: Optional[str] = None
    status: str = "pendente"  # "pendente" | "pago" | "cancelado"
    checkout_url: Optional[str] = None
    created_at: Optional[str] = None
