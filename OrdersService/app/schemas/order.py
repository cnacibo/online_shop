# OrdersService/app/schemas/order.py
from pydantic import BaseModel
from typing import List, Optional
from app.domain.enums import OrderStatus

class OrderCreate(BaseModel):
    amount: float
    description: str

class OrderStatusResponse(BaseModel):
    order_id: int
    status: OrderStatus

    class Config:
        from_attributes = True

class OrderResponse(BaseModel):
    id: int
    user_id: str
    amount: float
    description: str
    status: OrderStatus

    class Config:
        from_attributes = True
