# PaymentsService/app/infrastructure/inbox_processor.py
import asyncio
from sqlalchemy import select
from app.infrastructure.database import AsyncSessionLocal
from app.infrastructure.repositories import InboxEventModel
from app.use_cases.process_payment import process_payment
import json

async def process_inbox_events():
    while True:
        async with AsyncSessionLocal() as session:
            result = await session.execute(select(InboxEventModel).where(InboxEventModel.processed == False).limit(10))
            events = result.scalars().all()

            for event in events:
                payload = json.loads(event.payload)
                order_id = payload.get("order_id")
                user_id = payload.get("user_id")
                amount = payload.get("amount")

                # Выполняем оплату
                await process_payment(order_id, user_id, amount)

                event.processed = True
            await session.commit()

        await asyncio.sleep(2)
