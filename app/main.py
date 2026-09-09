from fastapi import FastAPI # Importando a classe FastAPI do módulo fastapi

app = FastAPI(title="Biblioteca NoSQL API") # Criando uma instância da aplicação FastAPI com o título "Biblioteca NoSQL API"

# IMportando os routers
from routers.health import health_router
from routers.books import books_router

app.include_router(health_router)
app.include_router(books_router)