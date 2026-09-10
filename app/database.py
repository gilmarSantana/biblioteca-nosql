import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env para o sistema
load_dotenv()

# Agora o os.environ conseguirá ler a URI perfeitamente
mongo_uri = os.environ.get("MONGO_URI")

client = MongoClient(mongo_uri)

db = client["biblioteca"]

if __name__ == "__main__":
    # Testando a conexão com o banco de dados
    try:
        client.admin.command('ping')
        print("Conexão com o MongoDB estabelecida com sucesso!")
    except Exception as e:
        print(f"Erro ao conectar ao MongoDB: {e}")