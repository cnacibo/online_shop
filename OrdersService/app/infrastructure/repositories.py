# OrdersService/app/infrastructure/repositories.py
from sqlalchemy import Column, Integer, String, Float, Enum, Boolean
from app.domain.entities import Order, OrderStatus
from app.domain.interfaces import OrderRepository
from app.infrastructure.database import AsyncSessionLocal, Base
from sqlalchemy import select
from sqlalchemy.dialects.postgresql import JSON

class OrderModel(Base):
    __tablename__ = "orders"
    __table_args__ = {"schema": "orders"}
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    amount = Column(Float)
    description = Column(String)
    status = Column(Enum(OrderStatus), default=OrderStatus.NEW, nullable=False)


class OrderRepositoryImpl(OrderRepository):
    async def save_order(self, order: Order) -> Order:
        async with AsyncSessionLocal() as session:
            db_order = OrderModel(**order.__dict__)
            session.add(db_order)
            await session.commit()
            await session.refresh(db_order)
            return Order(**db_order.__dict__)

    async def list_orders(self, user_id: str):
        async with AsyncSessionLocal() as session:
            result = await session.execute(select(OrderModel).where(OrderModel.user_id == user_id))
            orders = result.scalars().all()
            return [
                Order(
                    id=o.id,
                    user_id=o.user_id,
                    amount=o.amount,
                    description=o.description,
                    status=o.status
                )
                for o in orders
            ]

    async def get_order(self, order_id: int):
        async with AsyncSessionLocal() as session:
            result = await session.execute(select(OrderModel).where(OrderModel.id == order_id))
            db_order = result.scalar_one_or_none()
            if db_order:
                return Order(
                    id=db_order.id,
                    user_id=db_order.user_id,
                    amount=db_order.amount,
                    description=db_order.description,
                    status=db_order.status
                )
            return None

class OutboxEvent(Base):
    __tablename__ = "outbox"
    __table_args__ = {"schema": "orders"}

    id = Column(Integer, primary_key=True, index=True)
    event_type = Column(String)
    payload = Column(JSON)
    sent = Column(Boolean, default=False)
