from datetime import datetime
from bson import ObjectId
from domain.entities.doacao import Doacao
from domain.ports.doacao_repository import DoacaoRepository
from adapters.db.mongo_connection import get_collection


class MongoDoacaoRepository(DoacaoRepository):
    def __init__(self):
        self.collection = get_collection("doacoes")

    def save(self, doacao: Doacao) -> Doacao:
        payload = doacao.model_dump()
        payload.pop("id", None)
        payload["created_at"] = datetime.utcnow().isoformat()
        result = self.collection.insert_one(payload)
        doacao.id = str(result.inserted_id)
        return doacao

    def update_status(self, stripe_session_id: str, status: str) -> bool:
        result = self.collection.update_one(
            {"stripe_session_id": stripe_session_id},
            {"$set": {"status": status}},
        )
        return result.matched_count == 1
