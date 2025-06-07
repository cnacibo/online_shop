import aio_pika
import json
from app.infrastructure.database import AsyncSessionLocal
from app.infrastructure.repositories import OrderModel
from sqlalchemy import select

async def start_payment_result_consumer():
    connection = await aio_pika.connect_robust("amqp://guest:guest@rabbitmq/")
    channel = await connection.channel()
    queue = await channel.declare_queue("payments_to_orders", durable=True)

    async with queue.iterator() as queue_iter:
        async for message in queue_iter:
            async with message.process():
                data = json.loads(message.body)
                order_id = data.get("order_id")
                status = data.get("status")  # FINISHED / CANCELLED

                async with AsyncSessionLocal() as session:
                    result = await session.execute(select(OrderModel).where(OrderModel.id == order_id))
                    order = result.scalar_one_or_none()
                    if order:
                        order.status = status
                        await session.commit()