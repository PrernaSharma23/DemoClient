import time
import httpx
from typing import Dict

START_TIME = time.time()
VERSION = "1.0.0-client"
GATEWAY_URL = "http://localhost:8001"

async def _check_gateway() -> Dict:
    try:
        async with httpx.AsyncClient(timeout=2.0) as client:
            resp = await client.get(f"{GATEWAY_URL}/health")
            if resp.status_code == 200:
                return {"gateway": "ok"}
            else:
                return {"gateway": f"error:{resp.status_code}"}
    except Exception as e:
        return {"gateway": f"unreachable:{str(e)}"}

def _uptime_seconds() -> float:
    return time.time() - START_TIME

async def get_health() -> Dict:
    gateway_status = await _check_gateway()
    overall = "ok" if gateway_status.get("gateway") == "ok" else "degraded"
    return {
        "service": "client",
        "status": overall,
        "version": VERSION,
        "uptime_seconds": round(_uptime_seconds(), 2),
        "dependencies": gateway_status
    }
