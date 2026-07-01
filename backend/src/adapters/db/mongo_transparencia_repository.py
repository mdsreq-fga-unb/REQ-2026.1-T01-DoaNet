from typing import List

from bson import ObjectId
from pymongo import DESCENDING

from domain.entities.transparencia_record import TransparenciaRecord
from domain.ports.transparencia_repository import TransparenciaRepository
from adapters.db.mongo_connection import get_collection


class MongoTransparenciaRepository(TransparenciaRepository):
    def __init__(self, collection_handle=None) -> None:
        self.collection = collection_handle or get_collection("transparencia")

    def list_all(self) -> List[TransparenciaRecord]:
        """Retorna registros ordenados por data decrescente (CA-01)."""
        items = []
        for doc in self.collection.find().sort("data", DESCENDING):
            items.append(
                TransparenciaRecord(
                    id=str(doc["_id"]),
                    tipo=doc.get("tipo"),
                    valor=doc.get("valor"),
                    data=doc.get("data"),
                    descricao=doc.get("descricao"),
                    destino=doc.get("destino"),
                    created_at=doc.get("created_at"),
                    created_by=doc.get("created_by"),
                )
            )
        return items

    def add(self, record: TransparenciaRecord) -> None:
        """Insere registro. Imutável após inserção — sem update/delete."""
        if hasattr(record, "model_dump"):
            payload = record.model_dump()
        else:
            payload = record.dict()
        payload.pop("id", None)
        self.collection.insert_one(payload)
