from typing import Optional
from domain.entities.organization import Organization
from adapters.db.mongo_organization_repository import MongoOrganizationRepository

class OrganizationService:
    def __init__(self, repo: MongoOrganizationRepository):
        self.repo = repo

    def get_config(self, org_id: str) -> Optional[Organization]:
        return self.repo.find_by_org_id(org_id)

    def create_or_update(self, org: Organization) -> Organization:
        existing = self.repo.find_by_org_id(org.org_id)
        if existing:
            self.repo.update(org.org_id, org)
            return org
        return self.repo.create(org)