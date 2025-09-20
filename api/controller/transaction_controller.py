from fastapi import APIRouter, HTTPException
from models.transaction import Transaction
from services.transaction_service import TransactionService
from uuid import UUID

router = APIRouter()
transaction_service = TransactionService() 

@router.post("/transaction/{account_id}")
async def create_transaction(account_id: UUID, transaction_data: Transaction):
    response = transaction_service.create_transaction(account_id, transaction_data)
    
    if "error" in response:
        raise HTTPException(status_code=response["status_code"], detail=response["error"])
    
    return response 