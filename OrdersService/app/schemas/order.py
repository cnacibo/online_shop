from pydantic import BaseModel
from typing import List, Optional

class OrderCreate(BaseModel):
    items: List[str]
    total: float

class OrderStatusResponse(BaseModel):
    order_id: int
    status: str

class OrderResponse(BaseModel):
    id: int
    user_id: str
    status: str
    items: List[str]
    total: float
