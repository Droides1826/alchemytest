from utils.db import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Text, Numeric, DateTime, ForeignKey


class Proveedores(db.Model):
    __tablename__ = 'proveedores'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    direccion = db.Column(db.Text, nullable=True)
    
    productos = db.relationship('Producto', back_populates='proveedor')
    
    def __str__(self):
        return self.nombre
