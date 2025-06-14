# PaymentsService/app/api/routes.py
from fastapi import APIRouter, Depends, HTTPException
from app.schemas.account import AccountCreate, AccountResponse
from app.schemas.top_up import TopUpRequest, TopUpResponse
from app.schemas.balance import BalanceResponse
from app.schemas.payment import PaymentRequest, PaymentResponse
from app.use_cases.create_account import create_account
from app.use_cases.top_up_balance import top_up_balance
from app.use_cases.view_balance import view_balance
from app.use_cases.process_payment import process_payment
from app.api.dependencies import get_user_id

router = APIRouter()

@router.post("/account", response_model=AccountResponse)
async def create_account_route(user_id: str = Depends(get_user_id)):
    return await create_account(user_id)

@router.post("/account/top-up", response_model=TopUpResponse)
async def top_up_balance_route(request: TopUpRequest, user_id: str = Depends(get_user_id)):
    return await top_up_balance(user_id, request.amount)

@router.get("/account/balance", response_model=BalanceResponse)
async def view_balance_route(user_id: str = Depends(get_user_id)):
    return await view_balance(user_id)

@router.post("/payment", response_model=PaymentResponse)
async def process_payment_route(request: PaymentRequest, order_id: int, user_id: str = Depends(get_user_id)):
    status = await process_payment(order_id, user_id, request.amount)
    if status == "Payment successful":
        return PaymentResponse(status="SUCCESS", message="Payment was processed successfully")
    else:
        raise HTTPException(status_code=400, detail=status)
