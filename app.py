# client-service/app.py
from fastapi import FastAPI
import httpx

GATEWAY_URL = "http://localhost:8000"

app = FastAPI(title="Client Microservice")

@app.get("/client/user/{user_id}")
async def client_user(user_id: int):
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{GATEWAY_URL}/gateway/user/{user_id}")
        gateway_response = resp.json()

    if "error" in gateway_response:
        return gateway_response

    # Client depends on Gateway-transformed schema
    result = {
        "message": "Client successfully retrieved user!",
        "profile": {
            "id": gateway_response["userId"],
            "name": gateway_response["fullName"],
            "contact": gateway_response["contact"],
        }
    }

    return result
