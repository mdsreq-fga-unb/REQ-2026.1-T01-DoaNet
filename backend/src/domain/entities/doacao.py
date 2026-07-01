from typing import Optional
from pydantic import BaseModel


class Endereco(BaseModel):
    logradouro: Optional[str] = None       # Street Address
    complemento: Optional[str] = None      # Street Address Line 2
    cidade: Optional[str] = None           # City
    estado: Optional[str] = None           # Region/State/Province
    cep: Optional[str] = None              # Postal / Zip code (CEP)
    pais: Optional[str] = None             # Country


class Doacao(BaseModel):
    id: Optional[str] = None
    valor: float
    is_anonima: bool
    nome_doador: Optional[str] = None      # sempre coletado (usado na transparência)
    cpf: Optional[str] = None
    endereco: Optional[Endereco] = None
    direcao: str  # "instituicao" | "projeto"
    nome_projeto: Optional[str] = None
    stripe_session_id: Optional[str] = None
    stripe_payment_intent_id: Optional[str] = None
    status: str = "pendente"  # "pendente" | "pago" | "cancelado"
    checkout_url: Optional[str] = None
    # Dados obtidos do Stripe após confirmação do pagamento
    payment_status: Optional[str] = None
    payment_method: Optional[str] = None
    card_brand: Optional[str] = None
    card_last4: Optional[str] = None
    moeda: Optional[str] = None
    valor_total: Optional[float] = None
    stripe_info: Optional[dict] = None
    worm_path: Optional[str] = None
    created_at: Optional[str] = None
