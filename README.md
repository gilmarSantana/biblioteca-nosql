# Biblioteca NoSQL

API REST de consulta de livros, construída com FastAPI, MongoDB e PyMongo.

## Requisitos

- Python 3.10+
- Docker e Docker Compose

## Configuração

Crie um arquivo `.env` na raiz do projeto:

```env
MONGO_USER=admin
MONGO_PASSWORD=senha
MONGO_URI=mongodb://admin:senha@localhost:27017/?authSource=admin
```

As credenciais usadas em `MONGO_URI` devem ser as mesmas informadas em `MONGO_USER` e `MONGO_PASSWORD`.

## Executando

Instale as dependências e inicie o MongoDB:

```bash
python -m venv venv
# Windows PowerShell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
docker compose up -d
```

Inicie a API:

```bash
uvicorn app.main:app --reload
```

A aplicação ficará disponível em `http://localhost:8000`. A documentação interativa pode ser acessada em `/docs`.

## Endpoints

| Método | Rota | Descrição |
| --- | --- | --- |
| GET | `/health` | Verifica se o servidor está em execução |
| GET | `/books` | Lista todos os livros |
| GET | `/books/{book_id}` | Busca um livro pelo ObjectId do MongoDB |

Cada livro possui os campos `title`, `subtitle`, `authors`, `isbn` e `category`.

## Dados de exemplo

Com o MongoDB em execução, carregue os cinco livros de exemplo:

```bash
python scripts/seed_data.py
```

O script limpa a coleção `livros` antes de inserir os dados.

## Teste de carga

Para executar o cenário de carga que consulta `/books`:

```bash
locust -f locustfile.py
```

Depois, abra `http://localhost:8089`.
