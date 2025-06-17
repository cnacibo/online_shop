# PaymentsService/app/use_cases/top_up_balance.py
from app.infrastructure.repositories import AccountModel
from app.infrastructure.database import AsyncSessionLocal
from app.domain.entities import Account
from sqlalchemy import select
from fastapi import HTTPException, status



async def top_up_balance(user_id: str, amount: float):
    async with AsyncSessionLocal() as session:
        account = await session.execute(select(AccountModel).where(AccountModel.user_id == user_id))
        account = account.scalar_one_or_none()

        if not account:
            raise HTTPException(status_code=404, detail=f"Account for user {user_id} does not exist")

        if amount <= 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Top-up amount must be greater than zero"
            )

        account.balance += amount
        await session.commit()
        return Account(user_id=account.user_id, balance=account.balance)
