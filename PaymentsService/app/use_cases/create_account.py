# PaymentsService/app/use_cases/create_account.py
from app.infrastructure.repositories import AccountModel
from app.infrastructure.database import AsyncSessionLocal
from app.domain.entities import Account


async def create_account(user_id: str):
    async with AsyncSessionLocal() as session:
        account = AccountModel(user_id=user_id)
        session.add(account)
        await session.commit()
        await session.refresh(account)
        return Account(user_id=account.user_id, balance=account.balance)
