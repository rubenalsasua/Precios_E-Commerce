from fastapi import APIRouter, HTTPException
from datos import cargar_productos

router = APIRouter()

@router.get("/producto/{codigo}")
def obtener_producto(codigo: str):
    print("Cargando productos...")  # Debug
    productos = [p for p in cargar_productos() if p.codigo == codigo]
    print(f"Productos cargados: {len(productos)}")  # Debug
    if not productos:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    producto_reciente = max(productos, key=lambda p: p.fecha)
    return {
        "nombre": producto_reciente.nombre,
        "codigo": producto_reciente.codigo,
        "precio": producto_reciente.precio,
        "fecha": producto_reciente.fecha
    }