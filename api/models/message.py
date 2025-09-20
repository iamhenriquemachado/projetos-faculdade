class Message:
    # --- Default Error Messages ---
    ERROR_DEFAULT = "Um erro inesperado ocorreu. Por favor, tente novamente mais tarde."

   # --- Default Database Messages ---
    DATABASE_CONNECTED = "Conexão com o banco de dados realizada com sucesso."
    DATABASE_CONNECTION_FAILED = "Erro: Não foi possível conectar ao banco de dados."
    DATABASE_QUERY_FAILED = "Erro: Ocorreu um erro inesperado ao executar a query no banco de dados. Por favor verifique e tente novamente."

    # --- Default Transaction Messages ---
    TRANSACTION_USER_NOT_EXISTS = "O usuário informado não existe no banco de dados. Por favor verifique."
    TRANSACTION_INSUFICCIENT_BALANCE = "O usuário está com saldo insuficiente para realizar a operação."

MSG = Message()
