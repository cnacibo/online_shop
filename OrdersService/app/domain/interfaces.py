# OrdersService/app/domain/interfaces.py
from abc import ABC, abstractmethod
from typing import List
from .entities import Order

class OrderRepository(ABC):
    @abstractmethod
    async def save_order(self, order: Order) -> Order: pass

    @abstractmethod
    async def list_orders(self, user_id: str) -> List[Order]: pass

    @abstractmethod
    async def get_order(self, order_id: int) -> Order | None: pass

class OutboxPublisher(ABC):
    @abstractmethod
    async def publish_event(self, event_type: str, payload: dict): pass