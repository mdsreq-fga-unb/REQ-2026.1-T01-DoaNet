import pytest
import stripe
from fastapi import FastAPI
from fastapi.testclient import TestClient
from unittest.mock import MagicMock

from domain.entities.feed_item import FeedItem
from domain.entities.doacao import Doacao
import adapters.http.routes as routes


class FakeFeedRepository:
    def __init__(self) -> None:
        self.items = [
            FeedItem(
                id="1",
                title="Cesta basica",
                type="sem_evento",
                description="Doacao sem evento",
            ),
            FeedItem(
                id="2",
                title="Campanha do agasalho",
                type="com_evento",
                description="Doacao com evento vinculado",
            ),
        ]

    def list_all(self):
        return list(self.items)

    def add(self, item: FeedItem) -> None:
        data = item.model_dump() if hasattr(item, "model_dump") else item.dict()
        if not data.get("id"):
            data["id"] = str(len(self.items) + 1)
        self.items.append(FeedItem(**data))

    def update_item(self, item_id: str, item: FeedItem) -> bool:
        for idx, existing in enumerate(self.items):
            if existing.id == item_id:
                data = item.model_dump() if hasattr(item, "model_dump") else item.dict()
                data["id"] = item_id
                self.items[idx] = FeedItem(**data)
                return True
        return False

    def find_by_id(self, item_id: str):
        for item in self.items:
            if item.id == item_id:
                return item
        return None

    def delete(self, item_id: str) -> bool:
        for idx, existing in enumerate(self.items):
            if existing.id == item_id:
                del self.items[idx]
                return True
        return False


class FakeOportunidadeRepository:
    def __init__(self):
        self.items = []

    def list_all(self):
        return self.items

    def add(self, item):  
        self.items.append(item)
        return "fake-id-123"

    def update_item(self, item_id, item):  
        return True

    def delete(self, item_id):
        return True


class FakeGCSStorageService:
    def __init__(self, bucket_name: str):
        self.bucket_name = bucket_name

    def upload_image(self, file) -> dict:
        return {
            "image_url": "http://fake-storage.com/fake-image.jpg",
            "image_path": "feed/fake-image.jpg",
        }


class FakeDoacaoRepository:
    def __init__(self, collection_handle=None):
        self.saved = []
        self.updates = []

    def save(self, doacao: Doacao) -> Doacao:
        doacao.id = "fake-doacao-id"
        self.saved.append(doacao)
        return doacao

    def update_status(self, stripe_session_id: str, status: str) -> bool:
        self.updates.append((stripe_session_id, status))
        return True


class FakeAdminRepository:
    def __init__(self, collection_handle=None):
        self.admins = []

    async def create(self, admin):
        admin.id = "fake-admin-id"
        self.admins.append(admin)
        return admin

    async def find_by_email(self, email):
        return None

    async def find_by_id(self, admin_id):
        return None

    async def update_last_login(self, admin_id):
        pass

    async def count_admins(self):
        return 0

    async def list_all(self):
        return []

    async def update_role(self, admin_id, role):
        return True

    async def deactivate_admin(self, admin_id):
        return True

@pytest.fixture
def client(monkeypatch):
    monkeypatch.setattr(routes, "MongoFeedRepository", FakeFeedRepository)
    monkeypatch.setattr(routes, "MongoOportunidadeRepository", FakeOportunidadeRepository)
    monkeypatch.setattr(routes, "GCSStorageService", FakeGCSStorageService)
    monkeypatch.setattr(routes, "MongoAdminRepository", FakeAdminRepository)
    monkeypatch.setattr(routes, "MongoDoacaoRepository", FakeDoacaoRepository)
    app = FastAPI()
    app.include_router(routes.innit_routes())
    return TestClient(app)


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_get_feed(client):
    response = client.get("/feed")
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, list)
    assert len(payload) == 2
    assert payload[0]["id"] == "1"
    assert payload[0]["title"] == "Cesta basica"
    assert payload[0]["type"] == "sem_evento"
    assert payload[1]["type"] == "com_evento"


def test_add_feed_item(client):
    payload = {
        "title": "Mutirao de doacoes",
        "post_type": "com_evento",
        "description": "Campanha com evento",
    }

    response = client.post("/feed", data=payload)
    assert response.status_code == 200
    assert response.json() == {"message": "created"}

    feed = client.get("/feed").json()
    assert len(feed) == 3
    assert feed[-1]["type"] == "com_evento"


def test_update_feed_item(client):
    payload = {
        "title": "Cesta basica atualizada",
        "post_type": "com_evento",
        "description": "Atualizado",
    }

    response = client.put("/feed/1", data=payload)
    assert response.status_code == 200
    assert response.json() == {"message": "updated"}

    feed = client.get("/feed").json()
    assert feed[0]["title"] == "Cesta basica atualizada"
    assert feed[0]["type"] == "com_evento"


def test_delete_feed_item(client):
    response = client.delete("/feed/1")
    assert response.status_code == 200
    assert response.json() == {"message": "deleted"}

    response = client.delete("/feed/1")
    assert response.status_code == 200
    assert response.json() == {"message": "item not found"}


def test_get_oportunidades(client):
    response = client.get("/oportunidades")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_add_oportunidade(client):
    nova_vaga = {
        "titulo": "Professor de Reforço",
        "descricao": "Apoio escolar para alunos",
        "local": "Asa Norte",
        "horario": "Sábados, 14h às 16h",
        "vagas_totais": 10,
        "vagas_preenchidas": 0,
        "imagem_url": "http://foto.com/img.png",
        "ativo": True
    }
    response = client.post("/oportunidades", json=nova_vaga)
    assert response.status_code == 200


def test_update_oportunidade(client):
    vaga_atualizada = {
        "titulo": "Professor de Reforço Atualizado",
        "descricao": "Apoio escolar para alunos",
        "local": "Asa Norte",
        "horario": "Sábados, 14h às 16h",
        "vagas_totais": 10,
        "vagas_preenchidas": 1,
        "imagem_url": "http://foto.com/img.png",
        "ativo": True
    }
    response = client.put("/oportunidades/fake-id-123", json=vaga_atualizada)
    assert response.status_code == 200


def test_delete_oportunidade(client):
    response = client.delete("/oportunidades/fake-id-123")
    assert response.status_code == 200


# ============ TESTES DE DOAÇÕES ============
def test_checkout_retorna_url(client, monkeypatch):
    fake_session = MagicMock()
    fake_session.id = "cs_test_123"
    fake_session.url = "https://checkout.stripe.com/pay/cs_test_123"
    monkeypatch.setattr(stripe.checkout.Session, "create", lambda **kw: fake_session)

    response = client.post("/doacoes/checkout", json={
        "valor": 50.0,
        "is_anonima": False,
        "direcao": "instituicao",
    })

    assert response.status_code == 200
    assert response.json()["checkout_url"] == "https://checkout.stripe.com/pay/cs_test_123"


def test_checkout_com_projeto(client, monkeypatch):
    fake_session = MagicMock()
    fake_session.id = "cs_test_456"
    fake_session.url = "https://checkout.stripe.com/pay/cs_test_456"
    monkeypatch.setattr(stripe.checkout.Session, "create", lambda **kw: fake_session)

    response = client.post("/doacoes/checkout", json={
        "valor": 100.0,
        "is_anonima": True,
        "direcao": "projeto",
        "nome_projeto": "Aulas de Reforco",
    })

    assert response.status_code == 200
    assert "checkout_url" in response.json()


def test_webhook_evento_valido(client, monkeypatch):
    fake_event = {
        "type": "checkout.session.completed",
        "data": {"object": {"id": "cs_test_789"}},
    }
    monkeypatch.setattr(stripe.Webhook, "construct_event", lambda p, s, sec: fake_event)

    response = client.post(
        "/doacoes/webhook",
        content=b"payload",
        headers={"stripe-signature": "sig_valida"},
    )

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_webhook_assinatura_invalida_retorna_400(client, monkeypatch):
    def construir_com_erro(payload, sig, secret):
        raise stripe.error.SignatureVerificationError("invalido", sig)

    monkeypatch.setattr(stripe.Webhook, "construct_event", construir_com_erro)

    response = client.post(
        "/doacoes/webhook",
        content=b"payload_invalido",
        headers={"stripe-signature": "sig_errada"},
    )

    assert response.status_code == 400


def test_doacao_sucesso(client):
    response = client.get("/doacoes/sucesso")
    assert response.status_code == 200


def test_doacao_cancelado(client):
    response = client.get("/doacoes/cancelado")
    assert response.status_code == 200