import jwt
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, Security, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import os
from dotenv import load_dotenv

load_dotenv()

# Configurações do JWT
SECRET_KEY = os.getenv("JWT_SECRET_KEY", "sua_chave_secreta_aqui_mude_em_producao")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

security = HTTPBearer()

def create_access_token(data: dict):
    """Gera o token JWT."""
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    """Verifica se o token recebido na rota é válido."""
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido")

def get_current_user_email(payload: dict = Depends(verify_token)):
    """Extrai o email do usuário do token"""
    email = payload.get("sub")
    if not email:
        raise HTTPException(status_code=401, detail="Token inválido")
    return email

# Função para obter o repositório (DEFINIDA ANTES DE SER USADA)
async def get_admin_repository():
    from adapters.db.mongo_admin_repository import MongoAdminRepository
    return MongoAdminRepository()

# Agora podemos usar a função get_admin_repository
async def get_current_admin(
    credentials: HTTPAuthorizationCredentials = Security(security),
    admin_repo = Depends(get_admin_repository)
):
    """Retorna o admin atual a partir do token"""
    from domain.entities.admin import Admin
    
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if not email:
            raise HTTPException(status_code=401, detail="Token inválido")
        
        admin = await admin_repo.find_by_email(email)
        if not admin or not admin.is_active:
            raise HTTPException(status_code=401, detail="Admin não encontrado ou inativo")
        
        return admin
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido")

def require_master(admin = Depends(get_current_admin)):
    """Dependência para verificar se o admin é MASTER"""
    if admin.role != "master":
        raise HTTPException(status_code=403, detail="Acesso negado. Apenas administradores principais.")
    return admin