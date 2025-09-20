USE [TechMarket]
GO

/****** Object:  StoredProcedure [dbo].[proc_conta_detalhes]    Script Date: 20/09/2025 14:40:51 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

ALTER PROCEDURE [dbo].[proc_conta_detalhes]
    @ContaId UNIQUEIDENTIFIER,          -- conta específica
    @DataInicio DATETIME = NULL,        -- filtro inicial (opcional)
    @DataFim DATETIME = NULL            -- filtro final (opcional)
AS
BEGIN
    SET NOCOUNT ON;

    ----------------------------------------
    -- 1) Calcular saldo da conta
    ----------------------------------------
    SELECT 
        c.ContaId,
        c.NomeCompleto,
        ISNULL(SUM(
            CASE 
                WHEN t.TipoTransacao = 1 THEN t.Valor   -- Crédito
                WHEN t.TipoTransacao = 2 THEN -t.Valor  -- Débito
            END
        ), 0) AS SaldoFinal
    FROM Contas c
    LEFT JOIN Transacoes t ON t.ContaOrigemId = c.ContaId
        
    WHERE c.ContaId = @ContaId
	AND t.DataTransacao >= @DataInicio
	AND t.DataTransacao < @DataFim
    GROUP BY c.ContaId, c.NomeCompleto;

    ----------------------------------------
    -- 2) Listar 10 últimas transações da conta
    ----------------------------------------
    SELECT TOP 10
        t.TransacaoId,
        t.TipoTransacao,
        t.Valor,
        t.DataTransacao
    FROM Transacoes t
    WHERE t.ContaOrigemId = @ContaId
		AND t.DataTransacao >= @DataInicio
		AND t.DataTransacao < @DataFim
    ORDER BY t.DataTransacao DESC;
END
GO


