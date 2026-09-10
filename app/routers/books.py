from fastapi import APIRouter
from app.database import db  # Importando a instância do banco de dados do módulo database.py
from app.models.book import BookSchema

books_router = APIRouter(prefix="/books", tags=["Books"])

@books_router.get("", response_model=list[BookSchema])
def get_all_books():
    filter = {} # Um dict vazio significa "Trazer tudo"

    cursor = db.livros.find(filter) # Retorna um cursor, que é um iterador
    books = list(cursor) # Converte o cursor em uma lista de dicionários
    
    # Converte o tipo do campo _id, pois originalmente no mongo ele é do tipo ObjectId e o nosso BookModel requer uma str e a fastapi não consegue converter esse tipo para json para dar o retorno para o usuario da api
    for doc in books:
        doc['_id'] = str(doc['_id'])
    
    return books