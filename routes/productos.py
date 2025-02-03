from utils.db import db
from services.productos import Productos
from flask import request, jsonify
from flask import Blueprint

Productos = Blueprint('Productos', __name__)

@Productos.route('/productos', methods=['GET'])
def allproductos():
    productos = Productos.ObtenerProductos()
    return jsonify(productos)







