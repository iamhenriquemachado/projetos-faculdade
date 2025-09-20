-- Criar tabela Contas
CREATE TABLE Contas (
    ContaId UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(), -- UUID gerado automaticamente
    NomeCompleto NVARCHAR(150) NOT NULL,
    Email NVARCHAR(150) NOT NULL UNIQUE,
    Saldo DECIMAL(18,2) NOT NULL DEFAULT 0.00
);
