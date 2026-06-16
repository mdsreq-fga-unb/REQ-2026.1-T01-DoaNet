from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from adapters.http.routes import innit_routes

app = FastAPI(title="DoaNet Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=[""],
    allow_headers=["*"],
)

router = innit_routes()  # mutates the router by adding routes
app.include_router(router)