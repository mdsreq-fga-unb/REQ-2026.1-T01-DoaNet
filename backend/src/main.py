from fastapi import FastAPI
from routes.routes import router

app = FastAPI(title="DoaNet Backend")

app.include_router(router)