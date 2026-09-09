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
                "categoria": "Ciência da Computação",
                "preco": 65.00,
                "estoque": 12,
                "disponivel": True,
                "publicacao": {
                    "editora": "Novatec Editora",
                    "ano": 2017,
                    "paginas": 264,
                    "idioma": "Português"
                },
                "avaliacoes": {
                    "nota": 4.9,
                    "total_votos": 1280
                }
            },
            {
                "id": 2,
                "titulo": "Código Limpo",
                "subtitulo": "Habilidades Práticas do Agile Software",
                "autores": ["Robert C. Martin"],
                "isbn": "978-8576082675",
                "categoria": "Engenharia de Software",
                "preco": 95.50,
                "estoque": 5,
                "disponivel": True,
                "publicacao": {
                    "editora": "Alta Books",
                    "ano": 2009,
                    "paginas": 456,
                    "idioma": "Português"
                },
                "avaliacoes": {
                    "nota": 4.8,
                    "total_votos": 3410
                }
            },
            {
                "id": 3,
                "titulo": "Arquitetura Limpa",
                "subtitulo": "O Guia do Artesão para Estrutura e Design de Software",
                "autores": ["Robert C. Martin"],
                "isbn": "978-8550804606",
                "categoria": "Engenharia de Software",
                "preco": 89.90,
                "estoque": 0,
                "disponivel": False,
                "publicacao": {
                    "editora": "Alta Books",
                    "ano": 2019,
                    "paginas": 432,
                    "idioma": "Português"
                },
                "avaliacoes": {
                    "nota": 4.7,
                    "total_votos": 890
                }
            },
            {
                "id": 4,
                "titulo": "Padrões de Projetos",
                "subtitulo": "Soluções Reutilizáveis de Software Orientado a Objetos",
                "autores": ["Erich Gamma", "Richard Helm", "Ralph Johnson", "John Vlissides"],
                "isbn": "978-8573076103",
                "categoria": "Arquitetura de Software",
                "preco": 110.00,
                "estoque": 3,
                "disponivel": True,
                "publicacao": {
                    "editora": "Bookman",
                    "ano": 2000,
                    "paginas": 368,
                    "idioma": "Português"
                },
                "avaliacoes": {
                    "nota": 4.6,
                    "total_votos": 450
                }
            },
            {
                "id": 5,
                "titulo": "Python Fluente",
                "subtitulo": "Programação Clara, Concisa e Eficaz",
                "autores": ["Luciano Ramalho"],
                "isbn": "978-8575228623",
                "categoria": "Programação",
                "preco": 135.00,
                "estoque": 8,
                "disponivel": True,
                "publicacao": {
                    "editora": "Novatec Editora",
                    "ano": 2023,
                    "paginas": 1080,
                    "idioma": "Português"
                },
                "avaliacoes": {
                    "nota": 5.0,
                    "total_votos": 620
                }
            }
        ],
        "total": 5,
        "paginacao": {
            "pagina_atual": 1,
            "itens_por_pagina": 10,
            "total_paginas": 1
        }
    }
    return mock_livros_db