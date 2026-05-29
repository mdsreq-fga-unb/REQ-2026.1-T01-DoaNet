import os
import uuid

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

import adapters.http.routes as routes
from adapters.db.mongo_connection import get_collection


INTEGRATION_FLAG = "RUN_INTEGRATION_TESTS"


def _skip_if_disabled():
    if os.getenv(INTEGRATION_FLAG) != "1":
        pytest.skip(
            f"Integration tests disabled. Set {INTEGRATION_FLAG}=1 to enable."
        )


def _skip_if_mongo_unavailable():
    try:
        collection = get_collection()
        collection.database.client.admin.command("ping")
    except Exception as exc:
        pytest.skip(f"MongoDB not available: {exc}")


@pytest.fixture(scope="session")
def api_client():
    _skip_if_disabled()
    _skip_if_mongo_unavailable()

    app = FastAPI()
    app.include_router(routes.innit_routes())
    return TestClient(app)


@pytest.fixture()
def run_id():
    value = uuid.uuid4().hex
    yield value
    collection = get_collection()
    collection.delete_many(
        {
            "$or": [
                {"title": {"$regex": value}},
                {"description": {"$regex": value}},
            ]
        }
    )


@pytest.mark.integration
def test_health_integration(api_client):
    response = api_client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.integration
def test_feed_crud_flow(api_client, run_id):
    payload = {
        "title": f"IT_{run_id}",
        "type": "sem_evento",
        "description": f"Integracao {run_id}",
    }

    response = api_client.post("/feed", json=payload)
    assert response.status_code == 200
    assert response.json() == {"message": "created"}

    feed = api_client.get("/feed").json()
    created = next(item for item in feed if item["title"] == payload["title"])
    item_id = created["id"]

    update_payload = {
        "title": f"IT_{run_id}_atualizado",
        "type": "com_evento",
        "description": f"Atualizado {run_id}",
    }

    response = api_client.put(f"/feed/{item_id}", json=update_payload)
    assert response.status_code == 200
    assert response.json() == {"message": "updated"}

    feed = api_client.get("/feed").json()
    updated = next(item for item in feed if item["id"] == item_id)
    assert updated["title"] == update_payload["title"]
    assert updated["type"] == update_payload["type"]

    response = api_client.delete(f"/feed/{item_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "deleted"}

    feed = api_client.get("/feed").json()
    assert all(item["id"] != item_id for item in feed)
