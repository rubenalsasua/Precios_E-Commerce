from fastapi import FastAPI
from api import router as api_router

app = FastAPI(
    title="Análisis de Precios E-Commerce",
    description="API para consultar y analizar precios históricos de productos ficticios",
    version="1.0"
)

app.include_router(api_router)

@app.get("/")
def read_root():
    return {"mensaje": "Bienvenido a la API de análisis de precios"}
