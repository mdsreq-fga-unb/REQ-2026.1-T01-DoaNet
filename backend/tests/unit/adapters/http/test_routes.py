import pytest
import stripe
from fastapi import FastAPI
from fastapi.testclient import TestClient
from unittest.mock import MagicMock

from domain.entities.feed_item import FeedItem
from domain.entities.organization import Organization
from domain.entities.doacao import Doacao
from adapters.http.security import get_current_admin
from domain.entities.admin import Admin, AdminRole
import adapters.http.routes as routes


# ----------------------------------------------------------------------------
# Fakes
# ----------------------------------------------------------------------------
class FakeFeedRepository:
    def __init__(self) -> None:
        self.items = [
            FeedItem(id="1", title="Cesta basica", type="sem_evento",
                     description="Doacao sem evento", org_id="org-a"),
            FeedItem(id="2", title="Campanha do agasalho", type="com_evento",
                     description="Doacao com evento vinculado", org_id="org-b"),
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

    def upload_json(self, data, prefix="doacoes") -> dict:
        return {
            "worm_url": "http://fake-storage.com/worm/fake.json",
            "worm_path": "doacoes/fake.json",
        }


class FakeDoacaoRepository:
    def __init__(self, collection_handle=None):
        self.saved = []
        self.updates = []
        self.status_updates = []

    def save(self, doacao: Doacao) -> Doacao:
        doacao.id = "fake-doacao-id"
        self.saved.append(doacao)
        return doacao

    def update_status(self, stripe_session_id: str, status: str) -> bool:
        self.status_updates.append((stripe_session_id, status))
        return True

    def find_by_session_id(self, stripe_session_id: str):
        return Doacao(
            valor=50.0,
            is_anonima=False,
            nome_doador="Doador Teste",
            direcao="instituicao",
            stripe_session_id=stripe_session_id,
        )

    def update_by_session_id(self, stripe_session_id: str, campos: dict) -> bool:
        self.updates.append((stripe_session_id, campos))
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


class FakeOrganizationRepository:
    def __init__(self):
        self.items = []

    def find_by_org_id(self, org_id: str):
        for item in self.items:
            if item.org_id == org_id:
                return item
        return None

    def create(self, org: Organization) -> Organization:
        self.items.append(org)
        return org

    def update(self, org_id: str, org: Organization) -> bool:
        for idx, item in enumerate(self.items):
            if item.org_id == org_id:
                self.items[idx] = org
                return True
        return False


class FakeTransparenciaRepository:
    def __init__(self):
        self.items = []

    def list_all(self):
        return list(self.items)

    def add(self, record) -> None:
        self.items.append(record)


# ----------------------------------------------------------------------------
# Fixture
# ----------------------------------------------------------------------------
@pytest.fixture
def client(monkeypatch):
    monkeypatch.setattr(routes, "MongoFeedRepository", FakeFeedRepository)
    monkeypatch.setattr(routes, "MongoOportunidadeRepository", FakeOportunidadeRepository)
    monkeypatch.setattr(routes, "GCSStorageService", FakeGCSStorageService)
    monkeypatch.setattr(routes, "MongoAdminRepository", FakeAdminRepository)
    monkeypatch.setattr(routes, "MongoOrganizationRepository", FakeOrganizationRepository)
    monkeypatch.setattr(routes, "MongoTransparenciaRepository", FakeTransparenciaRepository)
    monkeypatch.setattr(routes, "MongoDoacaoRepository", FakeDoacaoRepository)

    fake_admin = Admin(
        email="master@test.com",
        name="Master",
        hashed_password="hash",
        role=AdminRole.MASTER,
        org_id=None,
    )

    app = FastAPI()
    app.dependency_overrides[get_current_admin] = lambda: fake_admin
    app.include_router(routes.innit_routes())
    return TestClient(app)


# ----------------------------------------------------------------------------
# Health
# ----------------------------------------------------------------------------
def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


# ----------------------------------------------------------------------------
# Feed
# ----------------------------------------------------------------------------
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


def test_get_feed_filtered_by_org_id(client):
    response = client.get("/feed?org_id=org-a")
    assert response.status_code == 200
    payload = response.json()
    assert len(payload) == 1
    assert payload[0]["title"] == "Cesta basica"


def test_get_feed_without_org_id_returns_all(client):
    response = client.get("/feed")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_feed_with_unknown_org_id_returns_empty(client):
    response = client.get("/feed?org_id=org-inexistente")
    assert response.status_code == 200
    assert response.json() == []


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


# ----------------------------------------------------------------------------
# Oportunidades
# ----------------------------------------------------------------------------
def test_get_oportunidades(client):
    response = client.get("/oportunidades")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_oportunidades_filtered_by_org_id(client):
    response = client.get("/oportunidades?org_id=org-inexistente")
    assert response.status_code == 200
    assert response.json() == []


def test_get_oportunidades_without_org_id_returns_all(client):
    client.post("/oportunidades", json={
        "titulo": "Vaga Teste",
        "descricao": "Desc",
        "local": "Local",
        "horario": "Sáb 9h",
        "vagas_totais": 5,
        "vagas_preenchidas": 0,
        "ativo": True,
    })

    response = client.get("/oportunidades")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_add_oportunidade(client):
    nova_vaga = {
        "titulo": "Professor de Reforço",
        "descricao": "Apoio escolar para alunos",
        "local": "Asa Norte",
        "horario": "Sábados, 14h às 16h",
        "vagas_totais": 10,
        "vagas_preenchidas": 0,
        "imagem_url": "http://foto.com/img.png",
        "ativo": True,
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
        "ativo": True,
    }
    response = client.put("/oportunidades/fake-id-123", json=vaga_atualizada)
    assert response.status_code == 200


def test_delete_oportunidade(client):
    response = client.delete("/oportunidades/fake-id-123")
    assert response.status_code == 200


# ----------------------------------------------------------------------------
# Organização
# ----------------------------------------------------------------------------
def test_get_org_config_not_found(client):
    response = client.get("/orgs/org-inexistente/config")
    assert response.status_code == 404


def test_create_org_and_get_config(client):
    response = client.post("/orgs", data={
        "org_id": "test-org",
        "name": "Org Teste",
        "description": "Descrição da org teste",
        "primary_color": "#FF0000",
        "background_color": "#FFFFFF",
    })
    assert response.status_code == 200
    assert response.json()["org_id"] == "test-org"

    response = client.get("/orgs/test-org/config")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Org Teste"
    assert data["primary_color"] == "#FF0000"
    assert data["description"] == "Descrição da org teste"


def test_update_org_config(client):
    client.post("/orgs", data={
        "org_id": "test-org",
        "name": "Org Teste",
        "description": "Descrição inicial",
        "primary_color": "#FF0000",
        "background_color": "#FFFFFF",
    })

    response = client.post("/orgs", data={
        "org_id": "test-org",
        "name": "Org Teste Atualizada",
        "description": "Descrição atualizada",
        "primary_color": "#00FF00",
        "background_color": "#FFFFFF",
    })
    assert response.status_code == 200

    response = client.get("/orgs/test-org/config")
    assert response.json()["name"] == "Org Teste Atualizada"
    assert response.json()["primary_color"] == "#00FF00"


def test_org_admin_cannot_configure_other_org(monkeypatch):
    """Admin comum não pode configurar org diferente da sua."""
    monkeypatch.setattr(routes, "MongoFeedRepository", FakeFeedRepository)
    monkeypatch.setattr(routes, "MongoOportunidadeRepository", FakeOportunidadeRepository)
    monkeypatch.setattr(routes, "MongoOrganizationRepository", FakeOrganizationRepository)
    monkeypatch.setattr(routes, "MongoTransparenciaRepository", FakeTransparenciaRepository)
    monkeypatch.setattr(routes, "MongoDoacaoRepository", FakeDoacaoRepository)
    monkeypatch.setattr(routes, "MongoAdminRepository", FakeAdminRepository)
    monkeypatch.setattr(routes, "GCSStorageService", FakeGCSStorageService)

    restricted_admin = Admin(
        email="admin@test.com",
        name="Admin",
        hashed_password="hash",
        role=AdminRole.ADMIN,
        org_id="minha-org",
    )

    app = FastAPI()
    app.dependency_overrides[get_current_admin] = lambda: restricted_admin
    app.include_router(routes.innit_routes())
    restricted_client = TestClient(app)

    response = restricted_client.post("/orgs", data={
        "org_id": "outra-org",
        "name": "Org Alheia",
        "description": "Não deveria conseguir",
        "primary_color": "#FF0000",
        "background_color": "#FFFFFF",
    })
    assert response.status_code == 403


def test_org_admin_can_configure_own_org(monkeypatch):
    """Admin comum pode configurar a própria org."""
    monkeypatch.setattr(routes, "MongoFeedRepository", FakeFeedRepository)
    monkeypatch.setattr(routes, "MongoOportunidadeRepository", FakeOportunidadeRepository)
    monkeypatch.setattr(routes, "MongoOrganizationRepository", FakeOrganizationRepository)
    monkeypatch.setattr(routes, "MongoTransparenciaRepository", FakeTransparenciaRepository)
    monkeypatch.setattr(routes, "MongoDoacaoRepository", FakeDoacaoRepository)
    monkeypatch.setattr(routes, "MongoAdminRepository", FakeAdminRepository)
    monkeypatch.setattr(routes, "GCSStorageService", FakeGCSStorageService)

    own_admin = Admin(
        email="admin@test.com",
        name="Admin",
        hashed_password="hash",
        role=AdminRole.ADMIN,
        org_id="minha-org",
    )

    app = FastAPI()
    app.dependency_overrides[get_current_admin] = lambda: own_admin
    app.include_router(routes.innit_routes())
    own_client = TestClient(app)

    response = own_client.post("/orgs", data={
        "org_id": "minha-org",
        "name": "Minha Org",
        "description": "Descrição",
        "primary_color": "#0088FF",
        "background_color": "#FFFFFF",
    })
    assert response.status_code == 200


# ----------------------------------------------------------------------------
# Doações (Stripe)
# ----------------------------------------------------------------------------
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

    fake_session = {
        "payment_status": "paid",
        "amount_total": 5000,
        "currency": "brl",
        "payment_intent": {"id": "pi_123", "status": "succeeded",
                           "payment_method": {"type": "card",
                                              "card": {"brand": "visa", "last4": "4242"}}},
    }
    monkeypatch.setattr(stripe.checkout.Session, "retrieve", lambda sid, **kw: fake_session)

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


def test_doacao_sucesso_com_session_id_confirma(client, monkeypatch):
    fake_session = {
        "payment_status": "paid",
        "amount_total": 5000,
        "currency": "brl",
        "payment_intent": {"id": "pi_redirect", "status": "succeeded",
                           "payment_method": {"type": "card",
                                              "card": {"brand": "visa", "last4": "4242"}}},
    }
    monkeypatch.setattr(stripe.checkout.Session, "retrieve", lambda sid, **kw: fake_session)

    response = client.get("/doacoes/sucesso?session_id=cs_test_redirect")
    assert response.status_code == 200


def test_doacao_cancelado(client):
    response = client.get("/doacoes/cancelado")
    assert response.status_code == 200