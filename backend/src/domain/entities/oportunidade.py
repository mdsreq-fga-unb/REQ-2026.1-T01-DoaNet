from typing import Optional
from pydantic import BaseModel

class OportunidadeVoluntariado(BaseModel):
    id: Optional[str] = None
    titulo: str
    descricao: str
    local: str
    horario: str
    vagas_totais: int            
    vagas_preenchidas: int = 0   
    imagem_url: Optional[str] = None
    ativo: bool = True