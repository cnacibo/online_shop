import asyncio
import aio_pika
import json

async def start_publisher():
    connection = await aio_pika.connect_robust("amqp://guest:guest@rabbitmq/")
    channel = await connection.channel()
    await channel.declare_queue("orders_to_payments", durable=True)
    # Заглушка — тут нужно реализовать Outbox-публикацию
    while True:
        await asyncio.sleep(10)