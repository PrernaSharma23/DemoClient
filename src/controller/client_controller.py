from fastapi import APIRouter
from service.client_service import get_client_user, get_client_users
from model.client_user_model import ClientUser, ClientUserList

router = APIRouter()

@router.get("/user/{user_id}", response_model=ClientUser)
async def user(user_id: int):
    return await get_client_user(user_id)

@router.get("/users", response_model=ClientUserList)
async def users():
    return await get_client_users()
