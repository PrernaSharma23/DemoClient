from fastapi import APIRouter
from service.health_service import get_health

router = APIRouter()

@router.get("/health")
async def health():
    """
    Client-level health: checks gateway dependency and optionally server via gateway.
    """
    return await get_health()
