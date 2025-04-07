from datetime import datetime
from pydantic import BaseModel

class Producto(BaseModel):
    nombre: str
    codigo: str
    precio: float
    fecha: datetime

class ProductoFactory:
    @staticmethod
    def crear_desde_fila_csv(fila: dict):
        return Producto(
            nombre=fila["Nombre"],
            codigo=fila["Código"],
            precio=float(fila["Precio"]),
            fecha=datetime.strptime(fila["Fecha"], "%Y-%m-%d %H:%M:%S")
        )
