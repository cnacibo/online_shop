# PaymentsService/app/infrastructure/inbox_consumer.py
import aio_pika
import json
from app.infrastructure.database import AsyncSessionLocal
from app.infrastructure.repositories import InboxEventModel

async def start_inbox_consumer():
    connection = await aio_pika.connect_robust("amqp://guest:guest@rabbitmq/")
    channel = await connection.channel()
    await channel.declare_queue("orders_to_payments", durable=True)

    async with channel.iterator() as queue_iter:
        async for message in queue_iter:
            async with message.process():
                data = json.loads(message.body)
                async with AsyncSessionLocal() as session:
                    inbox_event = InboxEventModel(
                        event_type="OrderCreated",
                        payload=json.dumps(data)
                    )
                    session.add(inbox_event)
                    await session.commit()

