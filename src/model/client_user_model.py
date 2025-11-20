from pydantic import BaseModel
from typing import List

class ClientUser(BaseModel):
    id: int
    name: str
    contact: str

class ClientUserList(BaseModel):
    users: List[ClientUser]
