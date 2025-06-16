# PaymentsService/app/infrastructure/inbox_consumer.py
import aio_pika
import json
from sqlalchemy import select
from app.infrastructure.database import AsyncSessionLocal
from app.infrastructure.repositories import InboxEventModel

async def start_inbox_consumer():
    connection = await aio_pika.connect_robust("amqp://guest:guest@rabbitmq/")
    channel = await connection.channel()
    queue = await channel.declare_queue("orders_to_payments", durable=True)

    async with queue.iterator() as queue_iter:
        async for message in queue_iter:
            async with message.process():
                data = json.loads(message.body)

                async with AsyncSessionLocal() as session:
                    inbox_event = InboxEventModel(
                        event_type="OrderCreated",
                        payload=json.dumps(data),  # Сохраняем как JSON строку
                    )
                    session.add(inbox_event)
                    await session.commit()


