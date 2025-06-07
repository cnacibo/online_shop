# OrdersService/app/domain/enums.py
from enum import Enum

class OrderStatus(str, Enum):
    NEW = "NEW"
    FINISHED = "FINISHED"
    CANCELLED = "CANCELLED"
