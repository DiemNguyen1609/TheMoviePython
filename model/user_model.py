from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    email: str

class UserInDB(User):
    id: str