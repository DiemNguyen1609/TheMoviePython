from fastapi import APIRouter, HTTPException
from model.model import User
from controller.controller import create_user, get_users, get_user, delete_user

router = APIRouter()

@router.post("/users/")
async def create(user: User):
    return create_user(user)

@router.get("/users/")
async def read_all():
    return get_users()

@router.get("/users/{user_id}")
async def read_one(user_id: str):
    user = get_user(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/users/{user_id}")
async def delete(user_id: str):
    if delete_user(user_id):
        return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")