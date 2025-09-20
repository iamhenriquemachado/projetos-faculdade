-- Criar tabela Transacoes
CREATE TABLE Transacoes (
    TransacaoId UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(), -- UUID gerado automaticamente
    TipoTransacao INT NOT NULL,  -- 1 = crédito, 2 = débito, etc
    ContaOrigemId UNIQUEIDENTIFIER NOT NULL,
    Valor DECIMAL(18,2) NOT NULL,
    DataTransacao DATETIME NOT NULL DEFAULT GETDATE(),
    CONSTRAINT FK_Transacoes_Contas FOREIGN KEY (ContaOrigemId) REFERENCES Contas(ContaId)
);
