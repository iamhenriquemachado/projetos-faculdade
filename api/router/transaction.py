from services.database import fetch_one, fetch_all, execute_commit
from fastapi import APIRouter, HTTPException
import logging
from models.message import MSG
from models.transaction import Transaction
from uuid import UUID

router = APIRouter()
logger = logging.getLogger("uvicorn")

@router.post("/transaction/{account_id}")
async def create_transaction(account_id: UUID, transaction_data: Transaction):

    # Checks if the user exists
    query_user_exists = f"SELECT ContaId FROM Contas WHERE ContaId = ?"
    params_user_exists = (account_id,)

    account_record = fetch_one(query_user_exists, params_user_exists)
        
    if account_record is None:
            logging.warning(MSG.TRANSACTION_USER_NOT_EXISTS)
            raise HTTPException(status_code=400, detail=MSG.TRANSACTION_USER_EXISTS)

    try:
        qry_check_balance = f"""SELECT 
                            SUM(
                                CASE 
                                    WHEN TipoTransacao = '1' THEN Valor   
                                    WHEN TipoTransacao = '2' THEN -Valor  
                                END
                            ) AS SaldoFinal
                        FROM 
                            Transacoes
                        WHERE 
                            ContaOrigemId = ?"""
        
        check_balance_record = fetch_one(qry_check_balance, params_user_exists)

        if check_balance_record <= 0 and transaction_data.tipo_transacao == 2:
            logging.warning(MSG.TRANSACTION_INSUFICCIENT_BALANCE)
            raise HTTPException(status_code=400, detail=MSG.TRANSACTION_INSUFICCIENT_BALANCE)

        insert_transaction = f"INSERT INTO Transacoes (TransacaoId,TipoTransacao,ContaOrigemId,Valor,DataTransacao) VALUES(?,?,?,?,?)"
        
        conta_origem = account_id

        params_transaction = (transaction_data.transacao_id, 
                              transaction_data.tipo_transacao, 
                             conta_origem, 
                              transaction_data.valor, 
                              transaction_data.data_transacao,)

        transaction_record = execute_commit(insert_transaction, params_transaction)

        if transaction_record == 0:
             raise HTTPException(status_code=400, detail=MSG.ERROR_DEFAULT)
        
        transaction_id_generated = transaction_data.transacao_id

    
        return {
            "message": MSG.SUCCESS_DEFAULT,
            "transaction_record": transaction_id_generated
        }
        
    except Exception as ex:
        logging.error(f"Error: {ex}")
        raise HTTPException(status_code=500, detail=MSG.ERROR_DEFAULT)