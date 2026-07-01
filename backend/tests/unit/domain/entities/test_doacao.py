import pytest
from pydantic import ValidationError

from domain.entities.doacao import Doacao


def test_doacao_aceita_campos_obrigatorios():
    d = Doacao(valor=50.0, is_anonima=False, direcao="instituicao")

    assert d.valor == 50.0
    assert d.is_anonima is False
    assert d.direcao == "instituicao"


def test_doacao_requer_valor():
    with pytest.raises(ValidationError):
        Doacao(is_anonima=False, direcao="instituicao")


def test_doacao_requer_direcao():
    with pytest.raises(ValidationError):
        Doacao(valor=50.0, is_anonima=False)


def test_doacao_status_padrao_e_pendente():
    d = Doacao(valor=10.0, is_anonima=True, direcao="projeto")

    assert d.status == "pendente"


def test_doacao_campos_opcionais_sao_none_por_padrao():
    d = Doacao(valor=10.0, is_anonima=True, direcao="instituicao")

    assert d.id is None
    assert d.nome_doador is None
    assert d.nome_projeto is None
    assert d.stripe_session_id is None
    assert d.checkout_url is None
    assert d.created_at is None


def test_doacao_aceita_campos_opcionais():
    d = Doacao(
        valor=75.0,
        is_anonima=False,
        nome_doador="Pedro",
        direcao="projeto",
        nome_projeto="Aulas de Reforco",
        stripe_session_id="cs_test_123",
        status="pago",
        checkout_url="https://checkout.stripe.com/pay/cs_test_123",
    )

    assert d.nome_doador == "Pedro"
    assert d.nome_projeto == "Aulas de Reforco"
    assert d.stripe_session_id == "cs_test_123"
    assert d.status == "pago"
