from datos import obtener_historial_producto

def buscar_producto_reciente(codigo_producto: str) -> dict:
    historial = obtener_historial_producto(codigo_producto)
    if not historial:
        return {}

    # El producto más reciente es el último en el historial (ya ordenado)
    producto_actual = historial[-1]
    
    # Obtener solo los precios históricos para incluir en la respuesta
    precios_historicos = [{"Precio": item["Precio"], "Fecha": item["Fecha"]} 
                          for item in historial]
    
    # Incluir el historial en la respuesta
    producto_actual["historial_precios"] = precios_historicos
    
    return producto_actual
