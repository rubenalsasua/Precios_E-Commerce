from datos import obtener_historial_producto

def buscar_producto_reciente(codigo_producto: str) -> dict:
    historial = obtener_historial_producto(codigo_producto)
    if not historial:
        return {}

    # Ordenar por fecha
    historial_ordenado = sorted(historial, key=lambda x: x["Fecha"])
    producto_actual = historial_ordenado[-1]
    return producto_actual
