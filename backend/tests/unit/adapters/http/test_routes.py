import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from unittest.mock import MagicMock

from domain.entities.feed_item import FeedItem
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

@pytest.fixture
def client(monkeypatch):
    monkeypatch.setattr(routes, "MongoFeedRepository", FakeFeedRepository)
    monkeypatch.setattr(routes, "MongoOportunidadeRepository", FakeOportunidadeRepository)
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