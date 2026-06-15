from datetime import datetime
from typing import Optional
from pymongo import MongoClient
from bson import ObjectId
from src.domain.ports.admin_repository import AdminRepository
from src.domain.entities.admin import Admin

class MongoAdminRepository(AdminRepository):
    def __init__(self, db: MongoClient):
        self.collection = db["admins"]
    
    async def create(self, admin: Admin) -> Admin:
        admin_dict = admin.dict(by_alias=True, exclude={"id"})
        result = self.collection.insert_one(admin_dict)
        admin.id = str(result.inserted_id)
        return admin
    
    async def find_by_email(self, email: str) -> Optional[Admin]:
        admin_dict = self.collection.find_one({"email": email})
        if admin_dict:
            return Admin(**admin_dict)
        return None
    
    async def find_by_id(self, admin_id: str) -> Optional[Admin]:
        try:
            admin_dict = self.collection.find_one({"_id": ObjectId(admin_id)})
            if admin_dict:
                return Admin(**admin_dict)
        except:
            pass
        return None
    
    async def update_last_login(self, admin_id: str) -> None:
        try:
            self.collection.update_one(
                {"_id": ObjectId(admin_id)},
                {"$set": {"last_login": datetime.utcnow()}}
            )
        except:
            pass
    
    async def count_admins(self) -> int:
        return self.collection.count_documents({})