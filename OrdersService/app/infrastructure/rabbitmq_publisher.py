# OrdersService/app/infrastructure/rabbitmq_publisher.py
import asyncio
import aio_pika
import json

import asyncio
import aio_pika
import json
from sqlalchemy import select
from app.infrastructure.repositories import OutboxEvent
from app.infrastructure.database import AsyncSessionLocal

async def start_publisher():
    connection = await aio_pika.connect_robust("amqp://guest:guest@rabbitmq/")
    channel = await connection.channel()
    queue = await channel.declare_queue("orders_to_payments", durable=True)

    while True:
        async with AsyncSessionLocal() as session:
            result = await session.execute(select(OutboxEvent).where(OutboxEvent.sent == 0).limit(10))
            events = result.scalars().all()
            for event in events:
                message = aio_pika.Message(body=event.payload.encode())
                await channel.default_exchange.publish(
                    message, routing_key="orders_to_payments"
                )
                event.sent = 1
            await session.commit()
        await asyncio.sleep(5)