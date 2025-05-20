from database.database import users_collection
from model.model import User
from bson import ObjectId

def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
    }

def create_user(user: User):
    result = users_collection.insert_one(user.dict())
    new_user = users_collection.find_one({"_id": result.inserted_id})
    return user_helper(new_user)

def get_users():
    return [user_helper(user) for user in users_collection.find()]

def get_user(user_id: str):
    user = users_collection.find_one({"_id": ObjectId(user_id)})
    return user_helper(user) if user else None

def delete_user(user_id: str):
    result = users_collection.delete_one({"_id": ObjectId(user_id)})
    return result.deleted_count > 0
