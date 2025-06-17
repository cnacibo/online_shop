# ApiGateway/app/api/dependencies.py
from fastapi import Header, HTTPException

async def get_user_id(user_id: str = Header(...)):
    if not user_id:
        raise HTTPException(status_code=400, detail="Missing user_id")
    return user_id
