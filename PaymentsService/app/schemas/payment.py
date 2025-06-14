# PaymentsService/app/schemas/payment.py
from pydantic import BaseModel

class PaymentRequest(BaseModel):
    order_id: int
    amount: float

class PaymentResponse(BaseModel):
    status: str
    message: str

    class Config:
        orm_mode = True
