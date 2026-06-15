from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.adapters.http.routes import init_routes

app = FastAPI(title="DoaNet Backend")

# Configuração CORS para permitir conexão do Streamlit
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8501", "http://127.0.0.1:8501"],  # Porta do Streamlit
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = init_routes()
app.include_router(router)