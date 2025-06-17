# PaymentsService/app/infrastructure/rabbitmq_publisher.py
import asyncio
import aio_pika
import json
from sqlalchemy import select
from app.infrastructure.repositories import OutboxEventModel
from app.infrastructure.database import AsyncSessionLocal
import logging
logger = logging.getLogger(__name__)

async def start_publisher():
    connection = await aio_pika.connect_robust("amqp://guest:guest@rabbitmq/")
    channel = await connection.channel()
    queue = await channel.declare_queue("payments_to_orders", durable=True)

    while True:
        async with AsyncSessionLocal() as session:
            result = await session.execute(select(OutboxEventModel).where(OutboxEventModel.sent == False).limit(10))
            events = result.scalars().all()
            for event in events:
                message = aio_pika.Message(body=json.dumps(event.payload).encode())
                logger.error(f"Sending a message about payment:) {message.body}")
                await channel.default_exchange.publish(message, routing_key="payments_to_orders")
                event.sent = True
            await session.commit()
        await asyncio.sleep(5)

