from fastapi import FastAPI

from adapters.http.routes import innit_routes

app = FastAPI(title="DoaNet Backend")

router = innit_routes()  # mutates the router by adding routes
app.include_router(router)