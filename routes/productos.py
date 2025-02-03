from flask import Blueprint, jsonify
from services.productos_queries import Productos_queries  
from models.Productos import Producto  

Productos_bp = Blueprint('Productos', __name__)  

@Productos_bp.route('/productos', methods=['GET'])
def obtener_productos():
    productos = Productos_queries.ObtenerProductos()  
    productos_json = [
        {
            "id": p.id,
            "nombre": p.nombre,
            "descripcion": p.descripcion,
            "cantidad": p.cantidad,
            "precio": float(p.precio),  
            "categoria_id": p.categoria_id,
            "proveedor_id": p.proveedor_id,
            "fecha_ingreso": p.fecha_ingreso.strftime('%Y-%m-%d')  
        }
        for p in productos
    ]
    return jsonify(productos_json)








