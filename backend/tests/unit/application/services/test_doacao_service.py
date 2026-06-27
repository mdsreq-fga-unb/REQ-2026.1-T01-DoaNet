from types import SimpleNamespace
from unittest.mock import MagicMock

import stripe

from application.services.doacao_service import DoacaoService
from domain.entities.doacao import Doacao


class FakeDoacaoRepository:
    def __init__(self):
        self.saved = []
        self.updates = []

    def save(self, doacao: Doacao) -> Doacao:
        doacao.id = "fake-doacao-id"
        self.saved.append(doacao)
        return doacao

    def update_status(self, stripe_session_id: str, status: str) -> bool:
        self.updates.append((stripe_session_id, status))
        return True


def _fake_session(session_id="cs_test_123", url="https://checkout.stripe.com/pay/cs_test_123"):
    s = MagicMock()
    s.id = session_id
    s.url = url
    return s


def test_criar_checkout_session_retorna_url(monkeypatch):
    monkeypatch.setattr(stripe.checkout.Session, "create", lambda **kw: _fake_session())

    repo = FakeDoacaoRepository()
    service = DoacaoService(repo)

    url = service.criar_checkout_session({
        "valor": 50.0,
        "is_anonima": False,
        "direcao": "instituicao",
    })

    assert url == "https://checkout.stripe.com/pay/cs_test_123"


def test_criar_checkout_session_salva_doacao_como_pendente(monkeypatch):
    monkeypatch.setattr(stripe.checkout.Session, "create", lambda **kw: _fake_session("cs_test_456"))

    repo = FakeDoacaoRepository()
    service = DoacaoService(repo)

    service.criar_checkout_session({
        "valor": 100.0,
        "is_anonima": True,
        "direcao": "projeto",
        "nome_projeto": "Aulas de Reforco",
    })

    assert len(repo.saved) == 1
    doacao = repo.saved[0]
    assert doacao.status == "pendente"
    assert doacao.stripe_session_id == "cs_test_456"
    assert doacao.nome_projeto == "Aulas de Reforco"
    assert doacao.is_anonima is True


def test_criar_checkout_session_converte_valor_para_centavos(monkeypatch):
    capturado = {}

    def fake_create(**kw):
        capturado.update(kw)
        return _fake_session()

    monkeypatch.setattr(stripe.checkout.Session, "create", fake_create)

    repo = FakeDoacaoRepository()
    service = DoacaoService(repo)
    service.criar_checkout_session({"valor": 49.99, "is_anonima": False, "direcao": "instituicao"})

    unit_amount = capturado["line_items"][0]["price_data"]["unit_amount"]
    assert unit_amount == 4999


def test_processar_webhook_marca_doacao_como_pago(monkeypatch):
    fake_event = {
        "type": "checkout.session.completed",
        "data": {"object": {"id": "cs_test_789"}},
    }
    monkeypatch.setattr(stripe.Webhook, "construct_event", lambda p, s, sec: fake_event)

    repo = FakeDoacaoRepository()
    service = DoacaoService(repo)
    service.processar_webhook(b"payload", "sig_header")

    assert repo.updates == [("cs_test_789", "pago")]


def test_processar_webhook_ignora_outros_eventos(monkeypatch):
    fake_event = {
        "type": "payment_intent.created",
        "data": {"object": {"id": "pi_123"}},
    }
    monkeypatch.setattr(stripe.Webhook, "construct_event", lambda p, s, sec: fake_event)

    repo = FakeDoacaoRepository()
    service = DoacaoService(repo)
    service.processar_webhook(b"payload", "sig_header")

    assert repo.updates == []


def test_processar_webhook_propaga_excecao_de_assinatura_invalida(monkeypatch):
    def construir_com_erro(payload, sig, secret):
        raise stripe.error.SignatureVerificationError("invalido", sig)

    monkeypatch.setattr(stripe.Webhook, "construct_event", construir_com_erro)

    repo = FakeDoacaoRepository()
    service = DoacaoService(repo)

    try:
        service.processar_webhook(b"payload_invalido", "sig_errada")
        assert False, "Deveria ter lancado excecao"
    except stripe.error.SignatureVerificationError:
        pass
