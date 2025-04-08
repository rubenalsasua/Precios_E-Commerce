from fastapi import APIRouter, HTTPException
from datos import cargar_productos, obtener_historial_producto

router = APIRouter()

@router.get("/producto/{codigo}")
def obtener_producto(codigo: str):
    print("Cargando productos...")  # Debug
    productos = [p for p in cargar_productos() if p.codigo == codigo]
    print(f"Productos cargados: {len(productos)}")  # Debug
    if not productos:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    # Mantener la lógica original para obtener el producto más reciente
    producto_reciente = max(productos, key=lambda p: p.fecha)
    resultado = {
        "nombre": producto_reciente.nombre,
        "codigo": producto_reciente.codigo,
        "precio": producto_reciente.precio,
        "fecha": producto_reciente.fecha
    }
    
    # Añadir el historial de precios
    historial = obtener_historial_producto(codigo)
    precios_historicos = [{"precio": item["Precio"], "fecha": item["Fecha"]} 
                          for item in historial]
    
    # Agregar el historial al resultado
    resultado["historial_precios"] = precios_historicos
    
    return resultado