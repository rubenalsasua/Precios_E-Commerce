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
