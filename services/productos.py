from utils.db import db
from models.Productos import Producto

class Productos:
    @staticmethod
    def ObtenerProductos():
        return Producto.query.all()

