# OrdersService/app/main.py
from fastapi import FastAPI
from app.api.routers import router
from app.infrastructure.database import create_db_and_tables
from app.infrastructure.rabbitmq_publisher import start_publisher
from app.infrastructure.payment_result_consumer import start_payment_result_consumer
import asyncio

app = FastAPI()
app.include_router(router)

@app.on_event("startup")
async def on_startup():
    await create_db_and_tables()
    asyncio.create_task(start_publisher())
    asyncio.create_task(start_payment_result_consumer())