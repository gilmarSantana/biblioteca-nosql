from fastapi import APIRouter

books_router = APIRouter(prefix="/books", tags=["Books"])

@books_router.get("")
def get_all_books():
    mock_livros_db = {
        "livros": [
            {
                "id": 1,
                "titulo": "Entendendo Algoritmos",
                "subtitulo": "Um Guia Ilustrado Para Programadores e Outros Curiosos",
                "autores": ["Aditya Y. Bhargava"],
                "isbn": "978-8575225639",
                "categoria": "Ciência da Computação"
            },
            {
                "id": 2,
                "titulo": "Código Limpo",
                "subtitulo": "Habilidades Práticas do Agile Software",
                "autores": ["Robert C. Martin"],
                "isbn": "978-8576082675",
                "categoria": "Engenharia de Software"
            },
            {
                "id": 3,
                "titulo": "Arquitetura Limpa",
                "subtitulo": "O Guia do Artesão para Estrutura e Design de Software",
                "autores": ["Robert C. Martin"],
                "isbn": "978-8550804606",
                "categoria": "Engenharia de Software"
            },
            {
                "id": 4,
                "titulo": "Padrões de Projetos",
                "subtitulo": "Soluções Reutilizáveis de Software Orientado a Objetos",
                "autores": ["Erich Gamma", "Richard Helm", "Ralph Johnson", "John Vlissides"],
                "isbn": "978-8573076103",
                "categoria": "Arquitetura de Software"
            },
            {
                "id": 5,
                "titulo": "Python Fluente",
                "subtitulo": "Programação Clara, Concisa e Eficaz",
                "autores": ["Luciano Ramalho"],
                "isbn": "978-8575228623",
                "categoria": "Programação"
            }
        ]
    }

   
    return mock_livros_db