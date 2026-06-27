from typing import Optional
from domain.entities.organization import Organization
from adapters.db.mongo_connection import get_collection

class MongoOrganizationRepository:
    def __init__(self):
        self.collection = get_collection("organizations")

    def find_by_org_id(self, org_id: str) -> Optional[Organization]:
        doc = self.collection.find_one({"org_id": org_id})
        if not doc:
            return None
        doc["id"] = str(doc.pop("_id"))
        return Organization(**doc)

    def create(self, org: Organization) -> Organization:
        data = org.model_dump(exclude={"id"})
        result = self.collection.insert_one(data)
        org.id = str(result.inserted_id)
        return org

    def update(self, org_id: str, org: Organization) -> bool:
        data = org.model_dump(exclude={"id"})
        result = self.collection.update_one(
            {"org_id": org_id},
            {"$set": data}
        )
        return result.modified_count > 0