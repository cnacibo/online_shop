# PaymentsService/app/schemas/payment.py
from pydantic import BaseModel
from app.domain.enums import PaymentStatus

class PaymentRequest(BaseModel):
    order_id: int
    amount: float

class PaymentResponse(BaseModel):
    status: PaymentStatus
    message: str

    class Config:
        orm_mode = True
