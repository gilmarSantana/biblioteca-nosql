from app.database import db  # Importando a instância do banco de dados do módulo database.py

mock_livros_db = {
        "livros": [
            {
                "title": "Entendendo Algoritmos",
                "subtitle": "Um Guia Ilustrado Para Programadores e Outros Curiosos",
                "authors": ["Aditya Y. Bhargava"],
                "isbn": "978-8575225639",
                "category": "Ciência da Computação"
            },
            {
                "title": "Código Limpo",
                "subtitle": "Habilidades Práticas do Agile Software",
                "authors": ["Robert C. Martin"],
                "isbn": "978-8576082675",
                "category": "Engenharia de Software"
            },
            {
                "title": "Arquitetura Limpa",
                "subtitle": "O Guia do Artesão para Estrutura e Design de Software",
                "authors": ["Robert C. Martin"],
                "isbn": "978-8550804606",
                "category": "Engenharia de Software"
            },
            {
                "title": "Padrões de Projetos",
                "subtitle": "Soluções Reutilizáveis de Software Orientado a Objetos",
                "authors": ["Erich Gamma", "Richard Helm", "Ralph Johnson", "John Vlissides"],
                "isbn": "978-8573076103",
                "category": "Arquitetura de Software"
            },
            {
                "title": "Python Fluente",
                "subtitle": "Programação Clara, Concisa e Eficaz",
                "authors": ["Luciano Ramalho"],
                "isbn": "978-8575228623",
                "category": "Programação"
            }
        ]
    }


if __name__ == "__main__":
    db.livros.delete_many({})  # Limpa a coleção antes de inserir os dados      
    db.livros.insert_many(mock_livros_db["livros"]) # Insere os dados do mock_livros_db na coleção "livros" do banco de dados
    print(f"{len(mock_livros_db['livros'])} livros inseridos com sucesso!")