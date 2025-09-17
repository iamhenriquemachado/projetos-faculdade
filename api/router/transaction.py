from services.database import fetch_one
from fastapi import APIRouter, HTTPException
import logging
from models.message import MSG

router = APIRouter()
logger = logging.getLogger("uvicorn")

@router.get("/transaction/{account_id}")
async def create_transaction(account_id: int):

    query_user_exists = f"SELECT ContaId FROM Contas WHERE ContaId = ?"
    params_user_exists = (account_id,)

    query_check_balance = f"SELECT Saldo From Contas WHERE ContaId = ?"


    try:
        account_record = fetch_one(query_user_exists, params_user_exists)
        
        if account_record is None:
            logging.warning(MSG.TRANSACTION_USER_EXISTS)
            raise HTTPException(status_code=400, detail=MSG.TRANSACTION_USER_EXISTS)
        
        account_id_from_db = account_record.ContaId
        return {
            "message": MSG.SUCCESS_DEFAULT, 
            "conta_id": account_id_from_db
        }
        
    except Exception as ex:
        logging.error(f"Error: {ex}")
        raise HTTPException(status_code=500, detail=MSG.ERROR_DEFAULT)