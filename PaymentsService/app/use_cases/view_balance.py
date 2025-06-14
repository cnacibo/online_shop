# PaymentsService/app/use_cases/view_balance.py
from app.infrastructure.repositories import AccountModel
from app.infrastructure.database import AsyncSessionLocal
from app.domain.entities import Account
from sqlalchemy import select
from fastapi import HTTPException


async def view_balance(user_id: str):
    async with AsyncSessionLocal() as session:
        account = await session.execute(select(AccountModel).where(AccountModel.user_id == user_id))
        account = account.scalar_one_or_none()

        if not account:
            raise HTTPException(status_code=404, detail=f"Account for user {user_id} does not exist")

        return Account(user_id=account.user_id, balance=account.balance)
