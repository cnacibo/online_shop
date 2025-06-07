from dataclasses import dataclass
from enum import Enum
from typing import List

class OrderStatus(str, Enum):
    PENDING = "PENDING"
    PAID = "PAID"
    FAILED = "FAILED"

@dataclass
class Order:
    id: int
    user_id: str
    items: List[str]
    total: float
    status: OrderStatus