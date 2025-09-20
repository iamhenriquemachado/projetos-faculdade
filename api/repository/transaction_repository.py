from services.database import fetch_one, execute_commit

class TransactionRepository:
    def get_account_by_id(self, account_id):
        query = "SELECT ContaId FROM Contas WHERE ContaId = ?"
        return fetch_one(query, (account_id,))

    def get_account_balance(self, account_id):
        query = """SELECT 
                    SUM(CASE WHEN TipoTransacao = '1' THEN Valor WHEN TipoTransacao = '2' THEN -Valor END) AS SaldoFinal
                   FROM Transacoes WHERE ContaOrigemId = ?"""
        result = fetch_one(query, (account_id,))

        return result.SaldoFinal if result and result.SaldoFinal else 0

    def insert_transaction(self, transaction_data, account_id):
        insert_transaction = "INSERT INTO Transacoes (TransacaoId,TipoTransacao,ContaOrigemId,Valor,DataTransacao) VALUES(?,?,?,?,?)"
        params_transaction = (
            transaction_data.transacao_id, 
            transaction_data.tipo_transacao, 
            account_id, 
            transaction_data.valor, 
            transaction_data.data_transacao,
        )
        # Retorna o ID da transação ou 0 em caso de falha
        return execute_commit(insert_transaction, params_transaction)