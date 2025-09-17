# TechMarket Finances - Sistema de Gestão Financeira Simplificado

![Status do Projeto](https://img.shields.io/badge/status-em--desenvolvimento-yellow)

Este repositório contém o código-fonte de um projeto integrado desenvolvido para o curso de **Análise e Desenvolvimento de Sistemas** da faculdade Unopar. O objetivo foi construir uma aplicação full-stack para simular transações financeiras básicas, aplicando conceitos de desenvolvimento back-end e front-end.

## ✨ Descrição do Projeto

A aplicação permite que um usuário realize transações financeiras, com o sistema validando o saldo disponível e registrando cada operação de forma segura. É uma demonstração prática de como criar uma API robusta com FastAPI e consumi-la com uma interface de usuário simples e funcional.

---

## 🚀 Funcionalidades Principais

O back-end da aplicação foi desenvolvido para atender aos seguintes requisitos:

-   [x] **Validação de Saldo:** Garante que o usuário possua saldo suficiente em sua conta bancária antes de autorizar uma nova transação.
-   [x] **Histórico de Transações:** Cada operação executada pelo usuário é devidamente registrada no sistema para futuras consultas.
-   [x] **Identificador Único (UUID):** Para garantir a rastreabilidade e a segurança, cada transação recebe um código único (UUID).

---

## 💻 Tecnologias Utilizadas

Este projeto foi construído utilizando as seguintes tecnologias:

-   **Back-end:**
    -   **Python 3.9+**
    -   **FastAPI:** Para a construção da API REST.
    -   **Uvicorn:** Como servidor ASGI para rodar a aplicação.
-   **Front-end:**
    -   **HTML5**
    -   **CSS3**
    -   **JavaScript**
    -   **Bootstrap 5:** Para a criação de uma interface responsiva.
-   **Ferramentas:**
    -   **Git & GitHub:** Para versionamento de código.

---

## 🔧 Instalação e Execução

Siga os passos abaixo para executar o projeto em sua máquina local.

**Pré-requisitos:**
* [Git](https://git-scm.com/)
* [Python 3.9](https://www.python.org/) ou superior

**1. Clone o repositório:**
```bash
git clone [https://github.com/](https://github.com/)[seu-usuario]/[nome-do-repositorio].git
cd [nome-do-repositorio]
```

**2. Configure e execute o Back-end:**
```bash
# Navegue até a pasta do back-end
cd backend

# Crie um ambiente virtual (recomendado)
python -m venv venv

# Ative o ambiente virtual
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Inicie o servidor
uvicorn main:app --reload
```
A API estará disponível em `http://127.0.0.1:3000`. Você pode acessar a documentação interativa em `http://127.0.0.1:3000/docs`.

**3. Execute o Front-end:**
O front-end é composto por arquivos estáticos. Basta abrir o arquivo principal no seu navegador:
-   Navegue até a pasta `frontend`.
-   Abra o arquivo `index.html` diretamente no seu navegador de preferência.

---

## 👨‍💻 Autor

Desenvolvido por **Henrique Machado**.

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
