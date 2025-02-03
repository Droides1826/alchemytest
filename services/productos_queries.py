from utils.db import db
from models.Productos import Producto

class Productos_queries:
    @staticmethod
    def ObtenerProductos():
        return Producto.query.all()

