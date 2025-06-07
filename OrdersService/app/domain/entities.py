# OrdersService/app/domain/entities.py
from dataclasses import dataclass
from typing import List
from app.domain.enums import OrderStatus

@dataclass
class Order:
    id: int
    user_id: str
    amount: float
    description: str
    status: OrderStatus


