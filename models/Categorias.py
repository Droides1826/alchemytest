from utils.db import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Text, Numeric, DateTime, ForeignKey


class Categorias(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    
    productos = db.relationship('Producto', back_populates='categoria')