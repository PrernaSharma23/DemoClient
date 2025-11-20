from fastapi import FastAPI
from controller.client_controller import router as client_router
from controller.health_controller import router as health_router

app = FastAPI(title="Client Microservice")

app.include_router(client_router, prefix="/client", tags=["Client"])
app.include_router(health_router, prefix="", tags=["Health"])
