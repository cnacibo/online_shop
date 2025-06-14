# PaymentsService/app/schemas/balance.py
from pydantic import BaseModel

class BalanceResponse(BaseModel):
    user_id: str
    balance: float

    class Config:
        orm_mode = True
