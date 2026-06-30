from types import SimpleNamespace
from bson import ObjectId
from adapters.db.mongo_organization_repository import MongoOrganizationRepository
from domain.entities.organization import Organization


class FakeCollection:
    def __init__(self, items=None):
        self.items = list(items or [])

    def find_one(self, filt):
        org_id = filt.get("org_id")
        for item in self.items:
            if item.get("org_id") == org_id:
                return dict(item)
        return None

    def insert_one(self, payload):
        stored = dict(payload)
        stored["_id"] = ObjectId()
        self.items.append(stored)
        return SimpleNamespace(inserted_id=stored["_id"])

    def update_one(self, filt, update):
        org_id = filt.get("org_id")
        matched = 0
        for item in self.items:
            if item.get("org_id") == org_id:
                item.update(update.get("$set", {}))
                matched = 1
                break
        return SimpleNamespace(modified_count=matched)


def _make_doc(**kwargs) -> dict:
    defaults = {
        "_id": ObjectId(),
        "org_id": "test-org",
        "name": "Org Teste",
        "description": "Descrição teste",
        "primary_color": "#FF0000",
        "background_color": "#FFFFFF",
        "logo_url": None,
    }
    defaults.update(kwargs)
    return defaults


def _make_org(**kwargs) -> Organization:
    defaults = {
        "org_id": "test-org",
        "name": "Org Teste",
        "description": "Descrição teste",
        "primary_color": "#FF0000",
        "background_color": "#FFFFFF",
        "logo_url": None,
    }
    defaults.update(kwargs)
    return Organization(**defaults)


# ----------------------------------------------------------------------------
# find_by_org_id
# ----------------------------------------------------------------------------
def test_find_by_org_id_returns_org():
    collection = FakeCollection([_make_doc()])
    repo = MongoOrganizationRepository(collection_handle=collection)

    org = repo.find_by_org_id("test-org")

    assert org is not None
    assert org.org_id == "test-org"
    assert org.name == "Org Teste"
    assert org.primary_color == "#FF0000"


def test_find_by_org_id_returns_none_when_missing():
    collection = FakeCollection()
    repo = MongoOrganizationRepository(collection_handle=collection)

    result = repo.find_by_org_id("nao-existe")

    assert result is None


def test_find_by_org_id_maps_id_correctly():
    oid = ObjectId()
    collection = FakeCollection([_make_doc(_id=oid)])
    repo = MongoOrganizationRepository(collection_handle=collection)

    org = repo.find_by_org_id("test-org")

    assert org.id == str(oid)


# ----------------------------------------------------------------------------
# create
# ----------------------------------------------------------------------------
def test_create_inserts_org():
    collection = FakeCollection()
    repo = MongoOrganizationRepository(collection_handle=collection)

    repo.create(_make_org())

    assert len(collection.items) == 1
    assert collection.items[0]["org_id"] == "test-org"


def test_create_returns_org_with_id():
    collection = FakeCollection()
    repo = MongoOrganizationRepository(collection_handle=collection)

    result = repo.create(_make_org())

    assert result.id is not None


def test_create_persists_all_fields():
    collection = FakeCollection()
    repo = MongoOrganizationRepository(collection_handle=collection)

    repo.create(_make_org(
        name="MoveEduca",
        description="Educação para todos",
        primary_color="#0088FF",
        logo_url="https://cdn.example.com/logo.png",
    ))

    saved = collection.items[0]
    assert saved["name"] == "MoveEduca"
    assert saved["description"] == "Educação para todos"
    assert saved["primary_color"] == "#0088FF"
    assert saved["logo_url"] == "https://cdn.example.com/logo.png"


# ----------------------------------------------------------------------------
# update
# ----------------------------------------------------------------------------
def test_update_returns_true_when_found():
    collection = FakeCollection([_make_doc()])
    repo = MongoOrganizationRepository(collection_handle=collection)

    result = repo.update("test-org", _make_org(name="Atualizada"))

    assert result is True


def test_update_modifies_fields():
    collection = FakeCollection([_make_doc()])
    repo = MongoOrganizationRepository(collection_handle=collection)

    repo.update("test-org", _make_org(name="Atualizada", primary_color="#00FF00"))

    assert collection.items[0]["name"] == "Atualizada"
    assert collection.items[0]["primary_color"] == "#00FF00"


def test_update_returns_false_when_missing():
    collection = FakeCollection()
    repo = MongoOrganizationRepository(collection_handle=collection)

    result = repo.update("nao-existe", _make_org())

    assert result is False


def test_update_does_not_affect_other_orgs():
    collection = FakeCollection([
        _make_doc(org_id="org-a", name="Org A"),
        _make_doc(org_id="org-b", name="Org B"),
    ])
    repo = MongoOrganizationRepository(collection_handle=collection)

    repo.update("org-a", _make_org(org_id="org-a", name="Org A Atualizada"))

    org_b = next(i for i in collection.items if i["org_id"] == "org-b")
    assert org_b["name"] == "Org B"