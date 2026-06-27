from types import SimpleNamespace

from bson import ObjectId

from adapters.db.mongo_doacao_repository import MongoDoacaoRepository
from domain.entities.doacao import Doacao


class FakeCollection:
    def __init__(self, items=None):
        self.items = list(items or [])

    def insert_one(self, payload):
        stored = dict(payload)
        stored["_id"] = ObjectId()
        self.items.append(stored)
        return SimpleNamespace(inserted_id=stored["_id"])

    def update_one(self, filt, update):
        key, val = next(iter(filt.items()))
        matched = 0
        for item in self.items:
            if item.get(key) == val:
                item.update(update.get("$set", {}))
                matched = 1
                break
        return SimpleNamespace(matched_count=matched)


def test_save_insere_documento_e_retorna_doacao_com_id():
    collection = FakeCollection()
    repo = MongoDoacaoRepository(collection_handle=collection)

    doacao = Doacao(valor=50.0, is_anonima=False, direcao="instituicao")
    resultado = repo.save(doacao)

    assert len(collection.items) == 1
    assert resultado.id is not None


def test_save_nao_inclui_campo_id_no_documento():
    collection = FakeCollection()
    repo = MongoDoacaoRepository(collection_handle=collection)

    doacao = Doacao(valor=50.0, is_anonima=False, direcao="instituicao")
    repo.save(doacao)

    assert "id" not in collection.items[0]


def test_save_preenche_created_at():
    collection = FakeCollection()
    repo = MongoDoacaoRepository(collection_handle=collection)

    doacao = Doacao(valor=30.0, is_anonima=True, direcao="projeto")
    repo.save(doacao)

    assert collection.items[0].get("created_at") is not None


def test_update_status_retorna_true_quando_session_encontrada():
    collection = FakeCollection([{
        "_id": ObjectId(),
        "stripe_session_id": "cs_test_abc",
        "status": "pendente",
    }])
    repo = MongoDoacaoRepository(collection_handle=collection)

    result = repo.update_status("cs_test_abc", "pago")

    assert result is True
    assert collection.items[0]["status"] == "pago"


def test_update_status_retorna_false_quando_session_nao_encontrada():
    collection = FakeCollection()
    repo = MongoDoacaoRepository(collection_handle=collection)

    result = repo.update_status("cs_test_inexistente", "pago")

    assert result is False
