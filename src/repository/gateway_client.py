import httpx
from fastapi import HTTPException

GATEWAY_URL = "http://localhost:8001"

async def gateway_get(path: str):
    url = f"{GATEWAY_URL}{path}"
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            resp = await client.get(url)
    except httpx.RequestError as e:
        raise HTTPException(status_code=503, detail=f"Gateway unreachable: {e}")

    if resp.status_code == 404:
        raise HTTPException(status_code=404, detail="Not found")
    if resp.status_code != 200:
        raise HTTPException(status_code=resp.status_code, detail="Upstream error")

    return resp.json()
