# PaymentsService/app/schemas/account.py
from pydantic import BaseModel

class AccountCreate(BaseModel):
    user_id: str

class AccountResponse(BaseModel):
    user_id: str
    balance: float

    class Config:
        orm_mode = True
