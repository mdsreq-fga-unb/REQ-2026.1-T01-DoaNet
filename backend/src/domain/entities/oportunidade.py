from typing import Optional
from pydantic import BaseModel

from domain.constants import DEFAULT_ORG_ID

class OportunidadeVoluntariado(BaseModel):
    id: Optional[str] = None
    titulo: str
    descricao: str
    local: str
    horario: str
    vagas_totais: int = 0
    vagas_preenchidas: int = 0
    link_inscricao: Optional[str] = None
    imagem_url: Optional[str] = None
    ativo: bool = True
    org_id: Optional[str] = DEFAULT_ORG_ID