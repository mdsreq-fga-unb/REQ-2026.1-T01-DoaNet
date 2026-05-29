import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

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


@pytest.fixture
def client(monkeypatch):
    monkeypatch.setattr(routes, "MongoFeedRepository", FakeFeedRepository)
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
