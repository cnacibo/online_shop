# ApiGateway/app/api/routers.py
from fastapi import APIRouter, UploadFile, File, HTTPException, Request, Body
from fastapi.responses import JSONResponse
import httpx
from typing import Dict, Any

router = APIRouter()

# URL микросервисов
ORDERS_SERVICE = "http://orders:8001"
PAYMENTS_SERVICE = "http://payments:8002"

async def make_service_request(
    method: str,
    service_url: str,
    endpoint: str,
    json: dict = None,
    params: dict = None,
    headers: dict = None
) -> Dict[str, Any]:
    url = f"{service_url}{endpoint}"
    async with httpx.AsyncClient(timeout=5.0) as client:
        response = await client.request(
            method=method,
            url=url,
            json=json,
            params=params,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()


# Orders Service

@router.post("/orders")
async def create_order(request: Request, payload: Dict[str, Any] = Body(...)):
    user_id = request.headers.get("user_id")
    if not user_id:
        raise HTTPException(status_code=400, detail="Missing user_id")

    response = await make_service_request(
        "POST",
        ORDERS_SERVICE,
        "/orders",
        json=payload,
        headers={"user_id": user_id}
    )
    return JSONResponse(content=response)

@router.get("/orders")
async def list_orders(request: Request):
    user_id = request.headers.get("user_id")
    if not user_id:
        raise HTTPException(status_code=400, detail="Missing user_id")

    response = await make_service_request(
        "GET",
        ORDERS_SERVICE,
        "/orders",
        headers={"user_id": user_id}
    )
    return JSONResponse(content=response)


@router.get("/orders/status/{order_id}")
async def get_order_status(order_id: str, request: Request):
    user_id = request.headers.get("user_id")
    if not user_id:
        raise HTTPException(status_code=400, detail="Missing user_id")

    response = await make_service_request(
        "GET",
        ORDERS_SERVICE,
        f"/orders/status/{order_id}",
        headers={"user_id": user_id}
    )
    return JSONResponse(content=response)



# Payments Service

@router.post("/account")
async def create_account(request: Request):
    user_id = request.headers.get("user_id")
    if not user_id:
        raise HTTPException(status_code=400, detail="Missing user_id")

    response = await make_service_request(
        "POST",
        PAYMENTS_SERVICE,
        "/account",
        headers={"user_id": user_id}
    )
    return JSONResponse(content=response)

@router.post("/account/add")
async def topup_account(request: Request, payload: Dict[str, Any] = Body(...)):
    user_id = request.headers.get("user_id")
    if not user_id:
        raise HTTPException(status_code=400, detail="Missing user_id")

    response = await make_service_request(
        "POST",
        PAYMENTS_SERVICE,
        "/account/add",
        json=payload,
        headers={"user_id": user_id}
    )
    return JSONResponse(content=response)

@router.get("/account/balance")
async def get_account_balance(request: Request):
    user_id = request.headers.get("user_id")
    if not user_id:
        raise HTTPException(status_code=400, detail="Missing user_id")

    response = await make_service_request(
        "GET",
        PAYMENTS_SERVICE,
        "/account/balance",
        headers={"user_id": user_id}
    )
    return JSONResponse(content=response)



