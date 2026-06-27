import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from domain.entities.feed_item import FeedItem
from domain.entities.organization import Organization
from adapters.http.security import get_current_admin
from domain.entities.admin import Admin, AdminRole
import adapters.http.routes as routes


# ----------------------------------------------------------------------------
# Fakes
# ----------------------------------------------------------------------------
class FakeFeedRepository:
    def __init__(self) -> None:
        self.items = [
            FeedItem(id="1", title="Cesta basica", type="sem_evento", description="Doacao sem evento"),
            FeedItem(id="2", title="Campanha do agasalho", type="com_evento", description="Doacao com evento vinculado"),
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


# ----------------------------------------------------------------------------
# Fixture
# ----------------------------------------------------------------------------
@pytest.fixture
def client(monkeypatch):
    monkeypatch.setattr(routes, "MongoFeedRepository", FakeFeedRepository)
    monkeypatch.setattr(routes, "MongoOportunidadeRepository", FakeOportunidadeRepository)
    monkeypatch.setattr(routes, "MongoOrganizationRepository", FakeOrganizationRepository)

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


def test_add_feed_item(client):
    payload = {
        "title": "Mutirao de doacoes",
        "type": "com_evento",
        "description": "Campanha com evento",
    }
    response = client.post("/feed", json=payload)
    assert response.status_code == 200
    assert response.json() == {"message": "created"}

    feed = client.get("/feed").json()
    assert len(feed) == 3
    assert feed[-1]["type"] == "com_evento"


def test_update_feed_item(client):
    payload = {
        "title": "Cesta basica atualizada",
        "type": "com_evento",
        "description": "Atualizado",
    }
    response = client.put("/feed/1", json=payload)
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
    from domain.entities.admin import Admin, AdminRole
    from adapters.http.security import get_current_admin

    monkeypatch.setattr(routes, "MongoFeedRepository", FakeFeedRepository)
    monkeypatch.setattr(routes, "MongoOportunidadeRepository", FakeOportunidadeRepository)
    monkeypatch.setattr(routes, "MongoOrganizationRepository", FakeOrganizationRepository)

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
    from domain.entities.admin import Admin, AdminRole
    from adapters.http.security import get_current_admin

    monkeypatch.setattr(routes, "MongoFeedRepository", FakeFeedRepository)
    monkeypatch.setattr(routes, "MongoOportunidadeRepository", FakeOportunidadeRepository)
    monkeypatch.setattr(routes, "MongoOrganizationRepository", FakeOrganizationRepository)

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