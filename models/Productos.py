from utils.db import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Text, Numeric, DateTime, ForeignKey


class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    cantidad = db.Column(db.Integer, nullable=True)
    precio = db.Column(db.Numeric(10,2), nullable=True)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=True)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedores.id'), nullable=True)
    fecha_ingreso = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    categoria = db.relationship('Categorias', back_populates='productos')
    proveedor = db.relationship('Proveedores', back_populates='productos')
    
    