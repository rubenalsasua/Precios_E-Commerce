import matplotlib.pyplot as plt
from datos import obtener_historial_producto
from datetime import datetime
import os

def generar_grafico_precios(codigo_producto: str, formato: str = "png") -> str:
    historial = obtener_historial_producto(codigo_producto)
    if not historial:
        return ""

    fechas = [datetime.strptime(reg["Fecha"], "%Y-%m-%d %H:%M:%S") for reg in historial]
    precios = [reg["Precio"] for reg in historial]

    plt.figure(figsize=(10, 5))
    plt.plot(fechas, precios, marker="o")
    plt.title(f"Evolución del precio - {historial[0]['Nombre']}")
    plt.xlabel("Fecha")
    plt.ylabel("Precio")
    plt.grid(True)

    carpeta_exportaciones = "exportaciones"
    os.makedirs(carpeta_exportaciones, exist_ok=True)
    ruta = os.path.join(carpeta_exportaciones, f"{codigo_producto}_grafico.{formato}")
    plt.tight_layout()
    plt.savefig(ruta)
    plt.close()

    return ruta
