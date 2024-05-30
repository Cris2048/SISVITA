from utils.db import db

class Usuarios(db.Model):
    __tablename__ = 'Usuarios'
    
    usuario_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=True)
    correo_electronico = db.Column(db.String(100), nullable=True)
    contrasena = db.Column(db.String(100), nullable=True)
    fecha_registro = db.Column(db.Date, nullable=True)

    def __init__(self, usuario_id, nombre, correo_electronico, contrasena, fecha_registro):
        self.usuario_id = usuario_id
        self.nombre = nombre
        self.correo_electronico = correo_electronico
        self.contrasena = contrasena
        self.fecha_registro = fecha_registro