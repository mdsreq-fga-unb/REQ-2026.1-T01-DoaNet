from typing import Optional, List
from bson import ObjectId
from datetime import datetime
from domain.ports.admin_repository import AdminRepository
from domain.entities.admin import Admin, AdminRole
from adapters.db.mongo_connection import get_collection

class MongoAdminRepository(AdminRepository):
    def __init__(self, collection_handle=None):
        self.collection = collection_handle or get_collection("admins")
    
    async def create(self, admin: Admin) -> Admin:
        admin_dict = admin.dict(by_alias=True, exclude={"id"})
        result = self.collection.insert_one(admin_dict)
        admin.id = str(result.inserted_id)
        return admin
    
    async def find_by_email(self, email: str) -> Optional[Admin]:
        admin_dict = self.collection.find_one({"email": email})
        if admin_dict:
            if "_id" in admin_dict:
                admin_dict["_id"] = str(admin_dict["_id"])
            return Admin(**admin_dict)
        return None
    
    async def find_by_id(self, admin_id: str) -> Optional[Admin]:
        try:
            admin_dict = self.collection.find_one({"_id": ObjectId(admin_id)})
            if admin_dict:
                if "_id" in admin_dict:
                    admin_dict["_id"] = str(admin_dict["_id"])
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
    
    async def list_all(self) -> List[Admin]:
        admins = []
        for admin_dict in self.collection.find():
            if "_id" in admin_dict:
                admin_dict["_id"] = str(admin_dict["_id"])
            admins.append(Admin(**admin_dict))
        return admins
    
    async def update_role(self, admin_id: str, role: str) -> bool:
        try:
            result = self.collection.update_one(
                {"_id": ObjectId(admin_id)},
                {"$set": {"role": role}}
            )
            return result.modified_count > 0
        except:
            return False
    
    async def deactivate_admin(self, admin_id: str) -> bool:
        try:
            result = self.collection.update_one(
                {"_id": ObjectId(admin_id)},
                {"$set": {"is_active": False}}
            )
            return result.modified_count > 0
        except:
            return False