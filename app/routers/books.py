from fastapi import APIRouter

books_router = APIRouter(prefix="/books", tags=["Books"])

@books_router.get("")
def get_all_books():
    mock_livros_db = {
        "livros": [
            {
                "id": 1,
                "title": "Entendendo Algoritmos",
                "subtitle": "Um Guia Ilustrado Para Programadores e Outros Curiosos",
                "authors": ["Aditya Y. Bhargava"],
                "isbn": "978-8575225639",
                "category": "Ciência da Computação"
            },
            {
                "id": 2,
                "title": "Código Limpo",
                "subtitle": "Habilidades Práticas do Agile Software",
                "authors": ["Robert C. Martin"],
                "isbn": "978-8576082675",
                "category": "Engenharia de Software"
            },
            {
                "id": 3,
                "title": "Arquitetura Limpa",
                "subtitle": "O Guia do Artesão para Estrutura e Design de Software",
                "authors": ["Robert C. Martin"],
                "isbn": "978-8550804606",
                "category": "Engenharia de Software"
            },
            {
                "id": 4,
                "title": "Padrões de Projetos",
                "subtitle": "Soluções Reutilizáveis de Software Orientado a Objetos",
                "authors": ["Erich Gamma", "Richard Helm", "Ralph Johnson", "John Vlissides"],
                "isbn": "978-8573076103",
                "category": "Arquitetura de Software"
            },
            {
                "id": 5,
                "title": "Python Fluente",
                "subtitle": "Programação Clara, Concisa e Eficaz",
                "authors": ["Luciano Ramalho"],
                "isbn": "978-8575228623",
                "category": "Programação"
            }
        ]
    }

   
    return mock_livros_db