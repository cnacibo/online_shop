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

class PaymentOutboxPayload(BaseModel):
    order_id: int
    user_id: str | None = None
    amount: float | None = None
    reason: str | None = None
    status: PaymentStatus
