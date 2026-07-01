from types import SimpleNamespace
from unittest.mock import MagicMock

import stripe

from application.services.doacao_service import DoacaoService
from domain.entities.doacao import Doacao


class FakeDoacaoRepository:
    def __init__(self, doacao_armazenada=None):
        self.saved = []
        self.updates = []
        self.campos_atualizados = []
        self.doacao_armazenada = doacao_armazenada

    def save(self, doacao: Doacao) -> Doacao:
        doacao.id = "fake-doacao-id"
        self.saved.append(doacao)
        return doacao

    def update_status(self, stripe_session_id: str, status: str) -> bool:
        self.updates.append((stripe_session_id, status))
        return True

    def find_by_session_id(self, stripe_session_id: str):
        return self.doacao_armazenada

    def update_by_session_id(self, stripe_session_id: str, campos: dict) -> bool:
        self.campos_atualizados.append((stripe_session_id, campos))
        return True


class FakeWormStorage:
    def __init__(self):
        self.registros = []

    def upload_json(self, data, prefix="doacoes"):
        self.registros.append((prefix, data))
        return {"worm_url": "http://fake/worm.json", "worm_path": "doacoes/fake.json"}


class FakeTransparenciaService:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)


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


def _fake_stripe_session_detalhada():
    return {
        "payment_status": "paid",
        "amount_total": 7500,
        "currency": "brl",
        "customer_details": {"name": "Pedro", "email": "pedro@test.com"},
        "payment_intent": {
            "id": "pi_abc",
            "status": "succeeded",
            "payment_method": {
                "type": "card",
                "card": {"brand": "visa", "last4": "4242"},
            },
        },
    }


def _mock_webhook_completed(monkeypatch, session_id="cs_test_worm"):
    fake_event = {
        "type": "checkout.session.completed",
        "data": {"object": {"id": session_id}},
    }
    monkeypatch.setattr(stripe.Webhook, "construct_event", lambda p, s, sec: fake_event)
    monkeypatch.setattr(
        stripe.checkout.Session, "retrieve",
        lambda sid, **kw: _fake_stripe_session_detalhada(),
    )


def test_processar_webhook_grava_worm_com_dados_stripe(monkeypatch):
    _mock_webhook_completed(monkeypatch)

    doacao = Doacao(valor=75.0, is_anonima=False, nome_doador="Pedro",
                    direcao="instituicao", stripe_session_id="cs_test_worm")
    repo = FakeDoacaoRepository(doacao_armazenada=doacao)
    worm = FakeWormStorage()
    transparencia = FakeTransparenciaService()
    service = DoacaoService(repo, worm_storage=worm, transparencia_service=transparencia)

    service.processar_webhook(b"payload", "sig_header")

    assert len(worm.registros) == 1
    prefix, registro = worm.registros[0]
    assert prefix == "doacoes"
    assert registro["tipo"] == "doacao_interna"
    assert registro["stripe"]["payment_status"] == "paid"
    assert registro["stripe"]["card_last4"] == "4242"
    assert registro["stripe"]["payment_method"] == "card"


def test_processar_webhook_cria_doacao_interna_na_transparencia(monkeypatch):
    _mock_webhook_completed(monkeypatch)

    doacao = Doacao(valor=75.0, is_anonima=False, nome_doador="Pedro",
                    direcao="instituicao", stripe_session_id="cs_test_worm")
    repo = FakeDoacaoRepository(doacao_armazenada=doacao)
    transparencia = FakeTransparenciaService()
    service = DoacaoService(repo, worm_storage=FakeWormStorage(),
                            transparencia_service=transparencia)

    service.processar_webhook(b"payload", "sig_header")

    assert len(transparencia.records) == 1
    record = transparencia.records[0]
    assert record.tipo.value == "doacao_interna"
    assert record.valor == 75.0
    assert "Pedro" in record.descricao


def test_processar_webhook_doacao_anonima_nao_expoe_nome(monkeypatch):
    _mock_webhook_completed(monkeypatch)

    doacao = Doacao(valor=30.0, is_anonima=True, nome_doador="Pedro",
                    direcao="instituicao", stripe_session_id="cs_test_worm")
    repo = FakeDoacaoRepository(doacao_armazenada=doacao)
    transparencia = FakeTransparenciaService()
    service = DoacaoService(repo, worm_storage=FakeWormStorage(),
                            transparencia_service=transparencia)

    service.processar_webhook(b"payload", "sig_header")

    record = transparencia.records[0]
    assert "Pedro" not in record.descricao
    assert "anônima" in record.descricao.lower()


def test_confirmar_pagamento_idempotente_nao_reprocessa(monkeypatch):
    monkeypatch.setattr(
        stripe.checkout.Session, "retrieve",
        lambda sid, **kw: _fake_stripe_session_detalhada(),
    )

    # Doação já confirmada (status "pago")
    doacao = Doacao(valor=50.0, is_anonima=False, nome_doador="Pedro",
                    direcao="instituicao", status="pago",
                    stripe_session_id="cs_test_worm")
    repo = FakeDoacaoRepository(doacao_armazenada=doacao)
    worm = FakeWormStorage()
    transparencia = FakeTransparenciaService()
    service = DoacaoService(repo, worm_storage=worm, transparencia_service=transparencia)

    service.confirmar_pagamento("cs_test_worm")

    assert worm.registros == []
    assert transparencia.records == []


def test_confirmar_pagamento_sem_session_id_nao_faz_nada():
    repo = FakeDoacaoRepository()
    service = DoacaoService(repo, worm_storage=FakeWormStorage(),
                            transparencia_service=FakeTransparenciaService())

    service.confirmar_pagamento("")

    assert repo.updates == []


def test_processar_webhook_persiste_dados_stripe_na_doacao(monkeypatch):
    _mock_webhook_completed(monkeypatch)

    doacao = Doacao(valor=75.0, is_anonima=False, nome_doador="Pedro",
                    direcao="instituicao", stripe_session_id="cs_test_worm")
    repo = FakeDoacaoRepository(doacao_armazenada=doacao)
    service = DoacaoService(repo, worm_storage=FakeWormStorage(),
                            transparencia_service=FakeTransparenciaService())

    service.processar_webhook(b"payload", "sig_header")

    assert len(repo.campos_atualizados) == 1
    _, campos = repo.campos_atualizados[0]
    assert campos["status"] == "pago"
    assert campos["payment_status"] == "paid"
    assert campos["card_last4"] == "4242"
    assert campos["worm_path"] == "doacoes/fake.json"
