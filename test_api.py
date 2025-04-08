import unittest
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from datetime import datetime
from main import app
from models import Producto

client = TestClient(app)

class TestAPI(unittest.TestCase):
    
    @patch('api.cargar_productos')
    @patch('api.obtener_historial_producto')
    def test_obtener_producto_existente(self, mock_historial, mock_cargar):
        # Configurar mocks
        producto_mock = Producto(
            nombre="Producto Test",
            codigo="TEST123",
            precio=99.99,
            fecha=datetime.strptime("2023-10-15 14:30:00", "%Y-%m-%d %H:%M:%S")
        )
        mock_cargar.return_value = [producto_mock]
        
        mock_historial.return_value = [
            {"Nombre": "Producto Test", "Código": "TEST123", "Precio": 129.99, "Fecha": "2023-08-10 09:00:00"},
            {"Nombre": "Producto Test", "Código": "TEST123", "Precio": 99.99, "Fecha": "2023-10-15 14:30:00"}
        ]
        
        # Realizar la solicitud
        response = client.get("/producto/TEST123")
        
        # Verificar resultado
        self.assertEqual(response.status_code, 200)
        data = response.json()
        
        # Verificar campos básicos
        self.assertEqual(data["nombre"], "Producto Test")
        self.assertEqual(data["codigo"], "TEST123")
        self.assertEqual(data["precio"], 99.99)
        
        # Verificar historial de precios
        self.assertIn("historial_precios", data)
        self.assertEqual(len(data["historial_precios"]), 2)
        self.assertEqual(data["historial_precios"][0]["precio"], 129.99)
    
    @patch('api.cargar_productos')
    def test_producto_no_encontrado(self, mock_cargar):
        # Configurar mock para retornar lista vacía (producto no encontrado)
        mock_cargar.return_value = []
        
        # Realizar la solicitud
        response = client.get("/producto/NOEXISTE")
        
        # Verificar respuesta
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"detail": "Producto no encontrado"})
    
    @patch('api.cargar_productos')
    @patch('api.obtener_historial_producto')
    def test_formato_respuesta(self, mock_historial, mock_cargar):
        # Configurar mocks
        producto_mock = Producto(
            nombre="Producto Test",
            codigo="TEST123",
            precio=99.99,
            fecha=datetime.strptime("2023-10-15 14:30:00", "%Y-%m-%d %H:%M:%S")
        )
        mock_cargar.return_value = [producto_mock]
        
        # Solo un precio en el historial
        mock_historial.return_value = [
            {"Nombre": "Producto Test", "Código": "TEST123", "Precio": 99.99, "Fecha": "2023-10-15 14:30:00"}
        ]
        
        # Realizar la solicitud
        response = client.get("/producto/TEST123")
        
        # Verificar resultado
        self.assertEqual(response.status_code, 200)
        data = response.json()
        
        # Verificar estructura completa de la respuesta
        self.assertIn("nombre", data)
        self.assertIn("codigo", data)
        self.assertIn("precio", data)
        self.assertIn("fecha", data)
        self.assertIn("historial_precios", data)
        
        # Verificar formato del historial
        historial = data["historial_precios"][0]
        self.assertIn("precio", historial)
        self.assertIn("fecha", historial)

if __name__ == "__main__":
    unittest.main()