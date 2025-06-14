# PaymentsService/app/use_cases/process_payment.py
from app.infrastructure.repositories import AccountModel, OutboxEventModel
from app.infrastructure.database import AsyncSessionLocal
from app.domain.entities import OutboxEvent, PaymentStatus
import json


async def process_payment(order_id: int, user_id: str, amount: float):
    async with AsyncSessionLocal() as session:
        # Проверка наличия счета
        account = await session.execute(select(AccountModel).where(AccountModel.user_id == user_id))
        account = account.scalar_one_or_none()

        if not account:
            event = OutboxEvent(event_type="PAYMENT_FAILED",
                                payload={"order_id": order_id, "reason": "Account not found"})
            session.add(OutboxEventModel(**event.__dict__))
            await session.commit()
            return "Account not found"

        if account.balance < amount:
            event = OutboxEvent(event_type="PAYMENT_FAILED",
                                payload={"order_id": order_id, "reason": "Insufficient balance"})
            session.add(OutboxEventModel(**event.__dict__))
            await session.commit()
            return "Insufficient balance"

        # Обновление баланса
        account.balance -= amount
        session.add(account)

        # Добавление события в outbox
        event = OutboxEvent(event_type="PAYMENT_SUCCESS",
                            payload={"order_id": order_id, "user_id": user_id, "amount": amount})
        session.add(OutboxEventModel(**event.__dict__))

        await session.commit()
        return "Payment successful"
