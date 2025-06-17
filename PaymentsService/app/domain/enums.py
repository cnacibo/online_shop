# PaymentsService/app/domain/enums.py
from enum import Enum

class PaymentStatus(str, Enum):
    FINISHED = "FINISHED"
    CANCELLED = "CANCELLED"
