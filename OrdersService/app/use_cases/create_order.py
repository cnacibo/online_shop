# OrdersService/app/use_cases/create_order.py
from app.domain.entities import Order, OrderStatus
from app.domain.interfaces import OrderRepository
from app.schemas.order import OrderCreate
from app.infrastructure.repositories import OrderModel, OutboxEvent, OrderRepositoryImpl
from app.infrastructure.database import AsyncSessionLocal
import json

async def create_order_use_case(user_id: str, data: OrderCreate):
    async with AsyncSessionLocal() as session:
        new_order = OrderModel(
            user_id=user_id,
            amount=data.amount,
            description=data.description,
            status=OrderStatus.NEW
        )
        session.add(new_order)
        await session.flush()

        outbox_event = OutboxEvent(
            event_type="OrderCreated",
            payload={
                "order_id": new_order.id,
                "user_id": user_id,
                "amount": data.amount
            },
            sent=False
        )
        session.add(outbox_event)

        await session.commit()
        await session.refresh(new_order)
        return Order(
            id=new_order.id,
            user_id=new_order.user_id,
            amount=new_order.amount,
            description=new_order.description,
            status=new_order.status
        )