import csv
from models import ProductoFactory

def cargar_productos(path_csv="datos.csv"):
    productos = []
    with open(path_csv, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for fila in reader:
            producto = ProductoFactory.crear_desde_fila_csv(fila)
            productos.append(producto)
    return productos

def obtener_historial_producto(codigo_producto: str, path_csv="datos.csv"):
    """
    Obtiene el historial de precios de un producto por su código
    
    Args:
        codigo_producto: El código único del producto
        path_csv: Ruta al archivo CSV con los datos
        
    Returns:
        Lista de diccionarios con el historial del producto, ordenado por fecha
    """
    historial = []
    productos = cargar_productos(path_csv)
    
    for producto in productos:
        if producto.codigo == codigo_producto:
            historial.append({
                "Nombre": producto.nombre,
                "Código": producto.codigo,
                "Precio": float(producto.precio),  # Convertir a float para cálculos
                "Fecha": producto.fecha
            })
    
    # Ordenar por fecha
    historial_ordenado = sorted(historial, key=lambda x: x["Fecha"])
    return historial_ordenado
