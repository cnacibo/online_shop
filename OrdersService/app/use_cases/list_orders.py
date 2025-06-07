from app.infrastructure.repositories import OrderRepositoryImpl

async def list_orders_use_case(user_id: str):
    repo = OrderRepositoryImpl()
    return await repo.list_orders(user_id)