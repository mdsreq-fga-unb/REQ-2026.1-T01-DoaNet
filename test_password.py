import os
import bcrypt
from pathlib import Path
from dotenv import load_dotenv
from pymongo import MongoClient
import certifi

# Tenta encontrar o .env em diferentes locais
possible_env_paths = [
    Path("backend/.env"),           # Se estiver na raiz
    Path(".env"),                   # Se estiver na mesma pasta
    Path("../backend/.env"),        # Se estiver dentro de backend
    Path(__file__).parent / "backend" / ".env",
    Path(__file__).parent / ".env",
]

env_loaded = False
for env_path in possible_env_paths:
    if env_path.exists():
        load_dotenv(env_path)
        print(f"✅ .env carregado de: {env_path}")
        env_loaded = True
        break

if not env_loaded:
    print("❌ Arquivo .env não encontrado!")
    print("Procurei em:", possible_env_paths)
    exit(1)

# Resto do código permanece igual...
MONGODB_USERNAME = os.getenv("MONGODB_USERNAME")
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
MONGODB_CLUSTER = os.getenv("MONGODB_CLUSTER")
MONGODB_DB_NAME = os.getenv("MONGODB_DB_NAME", "doa_net_db")

from urllib.parse import quote_plus
encoded_password = quote_plus(MONGODB_PASSWORD)
MONGODB_URI = f"mongodb+srv://{MONGODB_USERNAME}:{encoded_password}@{MONGODB_CLUSTER}/?retryWrites=true&w=majority"

client = MongoClient(MONGODB_URI, tlsCAFile=certifi.where())
db = client[MONGODB_DB_NAME]
collection = db["admins"]

# Email do admin que você criou
email = input("Digite o email do admin: ")

# Busca o admin
admin = collection.find_one({"email": email})

if not admin:
    print(f"❌ Admin com email {email} não encontrado!")
    exit()

print(f"✅ Admin encontrado: {admin['name']}")

# Testa senha
senha_teste = input("Digite a senha para testar: ")

# Recupera o hash armazenado
stored_hash = admin['hashed_password'].encode('utf-8')

# Verifica
if bcrypt.checkpw(senha_teste.encode('utf-8'), stored_hash):
    print("✅ SENHA CORRETA! O hash corresponde.")
else:
    print("❌ SENHA INCORRETA! O hash não corresponde.")
    print(f"\nHash armazenado: {admin['hashed_password']}")