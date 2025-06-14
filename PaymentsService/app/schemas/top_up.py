# PaymentsService/app/schemas/top_up.py
from pydantic import BaseModel

class TopUpRequest(BaseModel):
    amount: float

class TopUpResponse(BaseModel):
    user_id: str
    balance: float

    class Config:
        orm_mode = True
