# PaymentsService/app/use_cases/process_payment.py
from app.infrastructure.repositories import AccountModel, OutboxEventModel
from app.infrastructure.database import AsyncSessionLocal
from app.domain.entities import OutboxEvent
import json
from sqlalchemy import select

async def process_payment(order_id: int, user_id: str, amount: float):
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(AccountModel).where(AccountModel.user_id == user_id))
        account = result.scalar_one_or_none()

        if not account:
            event = OutboxEvent(
                event_type="PAYMENT_FAILED",
                payload={
                    "order_id": order_id,
                    "reason": "Account not found",
                    "status": "CANCELLED"
                }
            )
            session.add(OutboxEventModel(
                event_type=event.event_type,
                payload=json.dumps(event.payload),
                sent=event.sent
            ))
            await session.commit()
            return "Account not found"

        if account.balance < amount:
            event = OutboxEvent(
                event_type="PAYMENT_FAILED",
                payload={
                    "order_id": order_id,
                    "reason": "Insufficient balance",
                    "status": "CANCELLED"
                }
            )
            session.add(OutboxEventModel(
                event_type=event.event_type,
                payload=json.dumps(event.payload),
                sent=event.sent
            ))
            await session.commit()
            return "Insufficient balance"

        # Успешная оплата
        account.balance -= amount
        session.add(account)

        event = OutboxEvent(
            event_type="PAYMENT_SUCCESS",
            payload={
                "order_id": order_id,
                "user_id": user_id,
                "amount": amount,
                "status": "FINISHED"
            }
        )
        session.add(OutboxEventModel(
            event_type=event.event_type,
            payload=json.dumps(event.payload),
            sent=event.sent
        ))

        await session.commit()
        return "Payment successful"

