from fastapi import FastAPI # Importando a classe FastAPI do módulo fastapi

app = FastAPI(title="Biblioteca NoSQL API") # Criando uma instância da aplicação FastAPI com o título "Biblioteca NoSQL API"

# Importando os routers
from app.routers.health import health_router
from app.routers.books import books_router

# Incluindo os routers na aplicação FastAPI
app.include_router(health_router)
app.include_router(books_router)