import logging
from models.message import MSG
from repository.transaction_repository import TransactionRepository

logger = logging.getLogger("uvicorn")

class TransactionService:
    def __init__(self):
        # O serviço recebe uma instância do repositório
        self.repository = TransactionRepository()

    def create_transaction(self, account_id, transaction_data):
        # 1. Checa a existência da conta
        account_record = self.repository.get_account_by_id(account_id)
        if account_record is None:
            logging.warning(MSG.TRANSACTION_USER_NOT_EXISTS)
            return {"error": MSG.TRANSACTION_USER_EXISTS, "status_code": 400}
        
        # 2. Checa o saldo para saques
        if transaction_data.tipo_transacao == 2:
            balance = self.repository.get_account_balance(account_id)
            if balance <= 0:
                return {"error": MSG.TRANSACTION_INSUFICCIENT_BALANCE, "status_code": 400}
        
        # 3. Executa a transação no banco de dados
        try:
            transaction_id = self.repository.insert_transaction(transaction_data, account_id)
            if transaction_id == 0:
                return {"error": MSG.DATABASE_QUERY_FAILED, "status_code": 400}
            
            unique_id = transaction_data.transacao_id

            return {"message": MSG.SUCCESS_DEFAULT, "transaction_record": unique_id, "status_code": 201}
        
        except Exception as ex:
            logging.error(f"Error: {ex}")
            return {"error": MSG.ERROR_DEFAULT, "status_code": 500}