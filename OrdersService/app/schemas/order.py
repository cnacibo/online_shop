# OrdersService/app/schemas/order.py
from pydantic import BaseModel
from typing import List, Optional

class OrderCreate(BaseModel):
    amount: float
    description: str

class OrderStatusResponse(BaseModel):
    order_id: int
    status: str

class OrderResponse(BaseModel):
    id: int
    user_id: str
    amount: float
    description: str
    status: str
