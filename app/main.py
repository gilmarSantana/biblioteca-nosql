from fastapi import FastAPI # Importando a classe FastAPI do módulo fastapi
# Importando os routers
from app.routers.health import health_router
from app.routers.books import books_router


app = FastAPI(title="Biblioteca NoSQL API") # Criando uma instância da aplicação FastAPI


# Incluindo os routers na aplicação FastAPI
app.include_router(health_router)
app.include_router(books_router)