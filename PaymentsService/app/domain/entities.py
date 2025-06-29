# PaymentsService/app/domain/entities.py
from dataclasses import dataclass
from enum import Enum

@dataclass
class Account:
    user_id: str
    balance: float

@dataclass
class OutboxEvent:
    event_type: str
    payload: dict
    sent: bool = False
