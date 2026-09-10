from fastapi import APIRouter, status
from app.database import db  # Importando a instância do banco de dados do módulo database.py
from app.models.book import BookSchema
from bson import ObjectId
from bson.errors import InvalidId
from app.utils.errors import raise_api_error


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

@books_router.get("/{book_id}", response_model=BookSchema)
def get_book_by_id(book_id: str):
    
    try:
        object_id = ObjectId(book_id)
    except InvalidId:
        raise_api_error(status.HTTP_400_BAD_REQUEST, "O book_id informado está num formato inválido", "INVALID_BOOK_ID")       
     
    book = db.livros.find_one({"_id": object_id})
  
    if not book:
        raise_api_error(status.HTTP_404_NOT_FOUND, "Livro não encontrado", "BOOK_NOT_FOUND" )
                
    
    book['_id'] = str(book['_id'])
    
    return book
    
    