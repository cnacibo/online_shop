# PaymentsService/app/main.py
from fastapi import FastAPI
from app.api.routers import router
from app.infrastructure.rabbitmq_publisher import start_publisher

app = FastAPI()

app.include_router(router)

@app.on_event("startup")
async def on_startup():
    asyncio.create_task(start_publisher())
