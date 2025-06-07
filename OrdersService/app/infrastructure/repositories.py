from app.domain.entities import Order, OrderStatus
from app.domain.interfaces import OrderRepository
from app.infrastructure.database import AsyncSessionLocal, Base
from sqlalchemy import Column, Integer, String, Float, JSON, Enum, select

class OrderModel(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    items = Column(JSON)
    total = Column(Float)
    status = Column(Enum(OrderStatus), default=OrderStatus.PENDING)

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
            return [Order(**row.__dict__) for row in result.scalars().all()]

    async def get_order(self, order_id: int):
        async with AsyncSessionLocal() as session:
            result = await session.execute(select(OrderModel).where(OrderModel.id == order_id))
            db_order = result.scalar_one_or_none()
            return Order(**db_order.__dict__) if db_order else None