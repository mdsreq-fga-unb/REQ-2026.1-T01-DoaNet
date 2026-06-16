from types import SimpleNamespace

from bson import ObjectId

from adapters.db.mongo_feed_repository import MongoFeedRepository
from domain.entities.feed_item import FeedItem


class FakeCollection:
    def __init__(self, items=None):
        self.items = list(items or [])

    def find(self):
        return list(self.items)

    def insert_one(self, payload):
        stored = dict(payload)
        stored["_id"] = ObjectId()
        self.items.append(stored)
        return SimpleNamespace(inserted_id=stored["_id"])

    def update_one(self, filt, update):
        target_id = filt.get("_id")
        matched = 0
        for item in self.items:
            if item.get("_id") == target_id:
                item.update(update.get("$set", {}))
                matched = 1
                break
        return SimpleNamespace(matched_count=matched)

    def delete_one(self, filt):
        target_id = filt.get("_id")
        deleted = 0
        for idx, item in enumerate(self.items):
            if item.get("_id") == target_id:
                del self.items[idx]
                deleted = 1
                break
        return SimpleNamespace(deleted_count=deleted)


def test_list_all_returns_feed_items():
    oid = ObjectId()
    collection = FakeCollection(
        [
            {
                "_id": oid,
                "title": "Cesta basica",
                "type": "sem_evento",
                "description": "Doacao",
            }
        ]
    )

    repo = MongoFeedRepository(collection_handle=collection)
    items = repo.list_all()

    assert len(items) == 1
    assert items[0].id == str(oid)
    assert items[0].title == "Cesta basica"


def test_add_inserts_payload_without_id():
    collection = FakeCollection()
    repo = MongoFeedRepository(collection_handle=collection)

    item = FeedItem(id="123", title="Cesta basica", type="sem_evento", description="Doacao")
    repo.add(item)

    assert len(collection.items) == 1
    assert "id" not in collection.items[0]
    assert collection.items[0]["title"] == "Cesta basica"


def test_update_item_returns_true_when_found():
    oid = ObjectId()
    collection = FakeCollection(
        [
            {
                "_id": oid,
                "title": "Cesta basica",
                "type": "sem_evento",
                "description": "Doacao",
            }
        ]
    )

    repo = MongoFeedRepository(collection_handle=collection)
    updated = FeedItem(
        title="Cesta basica atualizada",
        type="com_evento",
        description="Atualizado",
    )

    result = repo.update_item(str(oid), updated)

    assert result is True
    assert collection.items[0]["title"] == "Cesta basica atualizada"


def test_update_item_returns_false_when_missing():
    collection = FakeCollection()
    repo = MongoFeedRepository(collection_handle=collection)

    updated = FeedItem(title="Cesta basica", type="sem_evento", description="Doacao")
    result = repo.update_item(str(ObjectId()), updated)

    assert result is False


def test_delete_returns_true_when_found():
    oid = ObjectId()
    collection = FakeCollection(
        [
            {
                "_id": oid,
                "title": "Cesta basica",
                "type": "sem_evento",
                "description": "Doacao",
            }
        ]
    )

    repo = MongoFeedRepository(collection_handle=collection)
    result = repo.delete(str(oid))

    assert result is True
    assert collection.items == []


def test_delete_returns_false_when_missing():
    collection = FakeCollection()
    repo = MongoFeedRepository(collection_handle=collection)

    result = repo.delete(str(ObjectId()))

    assert result is False
