# OrdersService/app/api/routers.py
from fastapi import APIRouter, Request, Depends, HTTPException
from app.schemas.order import OrderCreate, OrderResponse, OrderStatusResponse
from app.use_cases.create_order import create_order_use_case
from app.use_cases.list_orders import list_orders_use_case
from app.use_cases.get_order_status import get_order_status_use_case
from app.api.dependencies import get_user_id

router = APIRouter()

@router.post("/orders", response_model=OrderResponse)
async def create_order(payload: OrderCreate, user_id: str = Depends(get_user_id)):
    return await create_order_use_case(user_id, payload)

@router.get("/orders", response_model=list[OrderResponse])
async def list_orders(user_id: str = Depends(get_user_id)):
    return await list_orders_use_case(user_id)

@router.get("/orders/status/{order_id}", response_model=OrderStatusResponse)
async def get_status(order_id: int, user_id: str = Depends(get_user_id)):
    return await get_order_status_use_case(order_id)