SELECT 
    SUM(
        CASE 
            WHEN TipoTransacao = '1' THEN Valor   
            WHEN TipoTransacao = '2' THEN -Valor  
        END
    ) AS SaldoFinal
FROM 
    Transacoes
WHERE 
    ContaOrigemId = '?'