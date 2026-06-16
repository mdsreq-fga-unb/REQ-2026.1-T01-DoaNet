import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import bcrypt
from pymongo import MongoClient
import certifi
from datetime import datetime

# Adiciona o backend ao path para importar as configurações
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Carrega .env do backend
backend_dir = Path(__file__).resolve().parent / "backend"
if backend_dir.exists():
    load_dotenv(backend_dir / ".env")
else:
    load_dotenv(Path(__file__).resolve().parent / ".env")

# Configurações do MongoDB
MONGODB_USERNAME = os.getenv("MONGODB_USERNAME")
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
MONGODB_CLUSTER = os.getenv("MONGODB_CLUSTER")
MONGODB_DB_NAME = os.getenv("MONGODB_DB_NAME", "doa_net_db")

# Verifica se as configurações foram carregadas
print("🔍 Verificando configurações...")
print(f"MONGODB_USERNAME: {MONGODB_USERNAME}")
print(f"MONGODB_CLUSTER: {MONGODB_CLUSTER}")
print(f"MONGODB_DB_NAME: {MONGODB_DB_NAME}")

if not all([MONGODB_USERNAME, MONGODB_PASSWORD, MONGODB_CLUSTER]):
    print("❌ Configurações do MongoDB não encontradas no .env!")
    print("Certifique-se de que o arquivo .env existe e contém:")
    print("MONGODB_USERNAME=seu_usuario")
    print("MONGODB_PASSWORD=sua_senha")
    print("MONGODB_CLUSTER=ac-3jcqk5s.6iyf5br.mongodb.net")
    sys.exit(1)

# Dados do novo admin
NEW_ADMIN_EMAIL = input("Email do admin: ") or "joao.lelessouza@gmail.com"
NEW_ADMIN_NAME = input("Nome do admin: ") or "Joao Leles"
NEW_ADMIN_PASSWORD = input("Senha do admin: ") or "1234"

def hash_password(password: str) -> str:
    """Gera hash da senha"""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def create_admin():
    try:
        # Constrói a URI correta para MongoDB Atlas
        from urllib.parse import quote_plus
        encoded_password = quote_plus(MONGODB_PASSWORD)
        
        # URI para MongoDB Atlas
        MONGODB_URI = (
            f"mongodb+srv://{MONGODB_USERNAME}:{encoded_password}"
            f"@{MONGODB_CLUSTER}/?retryWrites=true&w=majority"
        )
        
        print(f"\n🔌 Conectando ao MongoDB Atlas...")
        print(f"Cluster: {MONGODB_CLUSTER}")
        
        # Conecta ao MongoDB Atlas
        client = MongoClient(
            MONGODB_URI,
            tlsCAFile=certifi.where(),
            serverSelectionTimeoutMS=10000  # 10 segundos
        )
        
        # Testa a conexão
        client.admin.command('ping')
        print("✅ Conectado ao MongoDB Atlas com sucesso!")
        
        db = client[MONGODB_DB_NAME]
        collection = db["admins"]
        
        # Verifica se admin já existe
        existing = collection.find_one({"email": NEW_ADMIN_EMAIL})
        if existing:
            print(f"\n⚠️ Admin com email {NEW_ADMIN_EMAIL} já existe!")
            print(f"ID: {existing['_id']}")
            print(f"Nome: {existing['name']}")
            
            # Pergunta se quer resetar a senha
            resposta = input("\nDeseja resetar a senha deste admin? (s/n): ")
            if resposta.lower() == 's':
                hashed_pw = hash_password(NEW_ADMIN_PASSWORD)
                collection.update_one(
                    {"email": NEW_ADMIN_EMAIL},
                    {"$set": {"hashed_password": hashed_pw}}
                )
                print(f"\n✅ Senha resetada com sucesso!")
                print(f"Email: {NEW_ADMIN_EMAIL}")
                print(f"Nova senha: {NEW_ADMIN_PASSWORD}")
            else:
                print("❌ Operação cancelada.")
            return
        
        # Cria novo admin
        hashed_password = hash_password(NEW_ADMIN_PASSWORD)
        admin_data = {
            "email": NEW_ADMIN_EMAIL,
            "name": NEW_ADMIN_NAME,
            "hashed_password": hashed_password,
            "is_active": True,
            "created_at": datetime.utcnow()
        }
        
        result = collection.insert_one(admin_data)
        print("\n✅ NOVO ADMINISTRADOR CRIADO COM SUCESSO!")
        print("-" * 50)
        print(f"ID: {result.inserted_id}")
        print(f"Email: {NEW_ADMIN_EMAIL}")
        print(f"Senha: {NEW_ADMIN_PASSWORD}")
        print(f"Nome: {NEW_ADMIN_NAME}")
        print("-" * 50)
        print("\n🔐 Use estas credenciais para fazer login no sistema!")
        
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        print("\n🔧 Possíveis soluções:")
        print("1. Verifique se as credenciais no .env estão corretas")
        print("2. Verifique se seu IP está na whitelist do MongoDB Atlas")
        print("3. Verifique se o cluster está ativo")

if __name__ == "__main__":
    print("=" * 50)
    print("🔄 CRIAR/RESETAR ADMINISTRADOR")
    print("=" * 50)
    create_admin()