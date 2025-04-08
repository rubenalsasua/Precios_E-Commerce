from datos import obtener_historial_producto

def verificar_alerta_precio_bajo(codigo_producto: str) -> dict:
    historial = obtener_historial_producto(codigo_producto)
    if not historial:
        return {"alerta": False, "mensaje": "Producto no encontrado"}

    precios = [registro["Precio"] for registro in historial]
    precio_actual = precios[-1]
    media = sum(precios) / len(precios)

    if precio_actual < media:
        return {
            "alerta": True,
            "mensaje": f"⚠️ El precio actual ({precio_actual}) es inferior a la media histórica ({media:.2f})"
        }
    else:
        return {
            "alerta": False,
            "mensaje": f"El precio actual ({precio_actual}) está por encima de la media histórica ({media:.2f})"
        }
