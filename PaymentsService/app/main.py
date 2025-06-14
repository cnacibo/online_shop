# PaymentsService/app/main.py
from fastapi import FastAPI
from app.api.routers import router
from app.infrastructure.rabbitmq_publisher import start_publisher
from app.infrastructure.database import create_db_and_tables
import asyncio
from app.infrastructure.inbox_consumer import start_inbox_consumer
from app.infrastructure.inbox_processor import process_inbox_events

app = FastAPI()

app.include_router(router)

@app.on_event("startup")
async def on_startup():
    await create_db_and_tables()
    asyncio.create_task(start_inbox_consumer())
    asyncio.create_task(process_inbox_events())
    asyncio.create_task(start_publisher())
