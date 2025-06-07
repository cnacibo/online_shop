from app.domain.entities import Order, OrderStatus
from app.domain.interfaces import OrderRepository
from app.schemas.order import OrderCreate
from app.infrastructure.repositories import OrderRepositoryImpl

async def create_order_use_case(user_id: str, data: OrderCreate):
    repo = OrderRepositoryImpl()
    new_order = Order(
        id=0,  # auto-generated
        user_id=user_id,
        items=data.items,
        total=data.total,
        status=OrderStatus.PENDING,
    )
    return await repo.save_order(new_order)