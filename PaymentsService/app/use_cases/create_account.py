# PaymentsService/app/use_cases/create_account.py
from app.infrastructure.repositories import AccountModel
from app.infrastructure.database import AsyncSessionLocal
from app.domain.entities import Account
from sqlalchemy import select
from fastapi import HTTPException, status


async def create_account(user_id: str):
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(AccountModel).where(AccountModel.user_id == user_id))
        existing_account = result.scalar_one_or_none()

        if existing_account:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Account for user '{user_id}' already exists."
            )


        account = AccountModel(user_id=user_id)
        session.add(account)
        await session.commit()
        await session.refresh(account)
        return Account(user_id=account.user_id, balance=account.balance)
