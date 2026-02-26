# FastAPI Zero 🚀

🌐 **Live Demo:** [Acesse a documentação da API aqui](https://fastapi-zero-chico.fly.dev/docs) 
*(Nota: O servidor entra em hibernação por inatividade. O primeiro acesso pode levar entre 5 e 10 segundos para carregar).*

Uma API RESTful moderna e assíncrona desenvolvida com FastAPI para gerenciamento de usuários e tarefas (To-Dos), com sistema de autenticação. 

Este projeto foi construído e aprimorado com base no curso "FastAPI do Zero", focando em boas práticas de desenvolvimento web com Python.

## 🛠️ Tecnologias Utilizadas

* **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
* **Linguagem:** Python 3.12
* **Gerenciador de Dependências:** [Poetry](https://python-poetry.org/)
* **Banco de Dados:** PostgreSQL (Driver Assíncrono: `asyncpg`)
* **ORM & Migrations:** SQLAlchemy + Alembic
* **Testes:** Pytest
* **Deploy:** [Fly.io](https://fly.io/) via Docker

## 📦 Estrutura do Projeto

A API possui as seguintes rotas principais:
* `/auth`: Geração e validação de tokens JWT.
* `/users`: Criação e gerenciamento de usuários.
* `/todos`: Criação, leitura, atualização e deleção de tarefas (vinculadas ao usuário autenticado).

## 🚀 Como rodar o projeto localmente

### Pré-requisitos
* Python 3.12+
* Poetry instalado
* Docker (para rodar o banco de dados local, opcional)

### Passo a passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/uChicoProgramming/Curso-FastAPI-dunossauro

2. **Ative o ambiente virtual e instale as dependencias:**
   ```bash
   poetry shell

   poetry install

3. **Configura as Variáveis de Ambiente:**
   ```bash
   DATABASE_URL="postgresql+asyncpg://usuario:senha@localhost:5432/nome_do_banco"
   SECRET_KEY="sua-chave-secreta-muito-segura"
   ALGORITHM="HS256"
   ACCESS_TOKEN_EXPIRE_MINUTES=30

4. **Execute as Migrações do Banco de Dados:**
   ```bash
   alembic upgrade head

5. **Inicie o Servidor:**
   ```bash
   task run

6. **Acesse a documentação:**
   Abra o navegador em http://localhost:8000/docs para interagir com o
Swagger UI.

###🧪 Como rodar os Testes

O projeto possui uma suíte de testes automatizados construídos com pytest para garantir a estabilidade da aplicação. Com o ambiente virtual ativo (poetry shell), você pode usar os atalhos do taskipy:

   ```bash
   task test
   ```
(Nota: O comando task test já deve estar configurado no fly.io. As variáveis de ambiente (como DATABASE_URL) são gerenciadas via Fly Secrets para garantirr a segurança das credenciais, e a conexão com o banco de dados em produção ultiliza a rede interna (.flycast).

☁️ Deploy

A aplicação está configurada para deploy contínuo no Fly.io. As variáveis de 
ambiente (como DATABASE_URL) são gerenciadas via Fly Secrets para garantir a 
segurança das credenciais, e a conexão com o banco de dados em produção 
utiliza a rede interna (.flycast).


