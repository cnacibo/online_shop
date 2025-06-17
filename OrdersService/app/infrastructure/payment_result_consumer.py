# OrdersService/app/infrastructure/payment_result_consumer.py
import aio_pika
import json
from app.infrastructure.database import AsyncSessionLocal
from app.infrastructure.repositories import OrderModel
from sqlalchemy import select
from app.domain.enums import OrderStatus
import logging
logger = logging.getLogger(__name__)

async def start_payment_result_consumer():
    connection = await aio_pika.connect_robust("amqp://guest:guest@rabbitmq/")
    channel = await connection.channel()
    queue = await channel.declare_queue("payments_to_orders", durable=True)

    async def handle_message(message: aio_pika.IncomingMessage):
        async with message.process():
            data = json.loads(message.body)
            order_id = data.get("order_id")
            status_str = data.get("status")

            try:
                status = OrderStatus(status_str)
            except ValueError as e:
                logger.warning(f"Unknown order status received: {status_str} for order_id={order_id} | ERROR: {e}")
                logger.error(f"Failed to parse message body: {message.body}")
                return


            async with AsyncSessionLocal() as session:
                result = await session.execute(select(OrderModel).where(OrderModel.id == order_id))
                order = result.scalar_one_or_none()
                if order:
                    order.status = status
                    await session.commit()
                else:
                    logger.warning(f"Order not found: order_id={order_id}")

    await queue.consume(handle_message)


