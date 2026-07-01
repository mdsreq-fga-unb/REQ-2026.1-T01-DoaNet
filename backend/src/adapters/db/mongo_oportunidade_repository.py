from bson import ObjectId

from domain.entities.oportunidade import OportunidadeVoluntariado
from domain.ports.oportunidade_repository import OportunidadeRepository
from domain.constants import DEFAULT_ORG_ID
from adapters.db.mongo_connection import get_collection, get_oportunidade_collection

class MongoOportunidadeRepository(OportunidadeRepository):
    def __init__(self, collection_handle=None) -> None:
        # Aqui chamamos a nova função que criamos no Passo 1!
        self.collection = collection_handle or get_collection('oportunidade_voluntariado')

    def list_all(self):
        items = []
        for item in self.collection.find():
            items.append(
                OportunidadeVoluntariado(
                    id=str(item["_id"]),
                    titulo=item.get("titulo", ""),
                    descricao=item.get("descricao", ""),
                    local=item.get("local", ""),
                    horario=item.get("horario", ""),
                    vagas_totais=item.get("vagas_totais", 0),
                    vagas_preenchidas=item.get("vagas_preenchidas", 0),
                    link_inscricao=item.get("link_inscricao"),
                    org_id=item.get("org_id") or DEFAULT_ORG_ID
                )
            )
        return items

    def add(self, item: OportunidadeVoluntariado) -> None:
        payload = item.model_dump() if hasattr(item, "model_dump") else item.dict()
        payload.pop("id", None)
        self.collection.insert_one(payload)

    def update_item(self, item_id: str, item: OportunidadeVoluntariado) -> bool:
        payload = item.model_dump() if hasattr(item, "model_dump") else item.dict()
        payload.pop("id", None)
        result = self.collection.update_one(
            {"_id": ObjectId(item_id)},
            {"$set": payload}
        )
        return result.matched_count == 1

    def delete(self, item_id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(item_id)})
        return result.deleted_count == 1