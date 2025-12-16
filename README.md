# FastAPI do Zero 🚀

Projeto de estudo, em andamento, sendo desenvolvido durante o curso "FastAPI do Zero" (por @dunossauro), focado em aprender desenvolvimento web moderno com Python, TDD (Test Driven Development) e boas práticas de engenharia de software.

## 🛠️ Tecnologias Utilizadas

Este projeto utiliza o que há de mais moderno no ecossistema Python:

- **[FastAPI](https://fastapi.tiangolo.com/):** Framework web moderno e de alta performance.
- **[Poetry](https://python-poetry.org/):** Gerenciamento de dependências e ambiente virtual.
- **[Ruff](https://docs.astral.sh/ruff/):** Linter e formatador de código extremamente rápido (substitui Black, Isort e Flake8).
- **[Pytest](https://docs.pytest.org/):** Framework de testes automatizados.
- **[Taskipy](https://github.com/taskipy/taskipy):** Automatizador de comandos (similar ao Makefile).

## 🔧 Como Rodar o Projeto

### Pré-requisitos
- Python 3.12+
- Poetry instalado

### Passo a passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU-USUARIO/fastapi_zero.git](https://github.com/SEU-USUARIO/fastapi_zero.git)
   cd fastapi_zero

2. **Instale as dependências:**
   ```bash
   poetry install

3. **Ative o ambiente virtual:**
   ```bash
   poetry shell

4. **Execute o servidor:**
   ```bash
   task run
  Após rodar o comando acesse
  - Aplicação: http://127.0.0.1:8000
  - Documentação Interativa (Swagger): http://127.0.0.1:8000/docs

### Comandos Úteis (Taskipy)

Os comandos foram simplificados através do `taskipy`:

- **`task lint`**: Verifica erros de estilo e código (Ruff check).
- **`task format`**: Formata o código automaticamente (Ruff format).
- **`task run`**: Roda o servidor de desenvolvimento (Uvicorn).
- **`task test`**: Roda os testes com relatório de cobertura (Pytest).
