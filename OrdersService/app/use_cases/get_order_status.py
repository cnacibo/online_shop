from app.infrastructure.repositories import OrderRepositoryImpl
from app.schemas.order import OrderStatusResponse

async def get_order_status_use_case(order_id: int):
    repo = OrderRepositoryImpl()
    order = await repo.get_order(order_id)
    return OrderStatusResponse(order_id=order.id, status=order.status)