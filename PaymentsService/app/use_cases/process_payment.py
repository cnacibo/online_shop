# PaymentsService/app/use_cases/process_payment.py
from app.infrastructure.repositories import AccountModel, OutboxEventModel
from app.infrastructure.database import AsyncSessionLocal
from app.schemas.payment import PaymentOutboxPayload
from app.domain.enums import PaymentStatus
import json
from sqlalchemy import select

import logging
logger = logging.getLogger(__name__)

async def process_payment(order_id: int, user_id: str, amount: float):
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(AccountModel).where(AccountModel.user_id == user_id))
        account = result.scalar_one_or_none()

        if not account:
            payload = PaymentOutboxPayload(
                order_id=order_id,
                reason="Account not found",
                status=PaymentStatus.CANCELLED
            ).model_dump(mode="json")

            logger.error(f"error: ❌ PAYMENT_FAILED: Account not found | order_id={order_id} user_id={user_id}")
            session.add(OutboxEventModel(
                event_type="PAYMENT_FAILED",
                payload=payload,
                sent=False
            ))
            await session.commit()
            return "Account not found"


        if account.balance < amount:
            payload = PaymentOutboxPayload(
                order_id=order_id,
                reason="Insufficient balance",
                status=PaymentStatus.CANCELLED
            ).model_dump(mode="json")

            logger.error(f"error: ❌ PAYMENT_FAILED: Insufficient balance | order_id={order_id} user_id={user_id} balance={account.balance} required={amount}")
            session.add(OutboxEventModel(
                event_type="PAYMENT_FAILED",
                payload=payload,
                sent=False
            ))
            await session.commit()
            return "Insufficient balance"

        # Успешная оплата
        account.balance -= amount
        session.add(account)

        payload = PaymentOutboxPayload(
            order_id=order_id,
            user_id=user_id,
            amount=amount,
            status=PaymentStatus.FINISHED
        ).model_dump(mode="json")


        session.add(OutboxEventModel(
            event_type="PAYMENT_SUCCESS",
            payload=payload,
            sent=False
        ))

        await session.commit()
        return "Payment successful"