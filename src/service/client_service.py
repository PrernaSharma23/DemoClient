from repository.gateway_client import gateway_get
from model.client_user_model import ClientUser, ClientUserList

async def get_client_user(user_id: int):
    data = await gateway_get(f"/gateway/user/{user_id}")
    return ClientUser(
        id=data["userId"],
        name=data["fullName"],
        contact=data["contact"],
    )

async def get_client_users():
    raw = await gateway_get("/gateway/users")
    users = [
        ClientUser(
            id=u["userId"],
            name=u["fullName"],
            contact=u["contact"]
        )
        for u in raw["users"]
    ]
    return ClientUserList(users=users)
