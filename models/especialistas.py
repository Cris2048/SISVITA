from utils.db import db

class Especialistas(db.Model):
    __tablename__ = 'Especialistas'
    especialista_id = db.Column(db.Integer(), primary_key = True)
    nombre = db.Column(db.String(100))
    titulo = db.Column(db.String(100))
    correo_electronico = db.Column(db.String(100))
    contrasena = db.Column(db.String(50))
    horarios_disponibilidad = db.Column(db.String(100), nullable=True)

    def __init__(self, especialista_id, nombre, titulo, correo_electronico, contrasena, horarios_disponibilidad=None):
        self.especialista_id = especialista_id
        self.nombre = nombre
        self.titulo = titulo
        self.correo_electronico = correo_electronico
        self.contrasena = contrasena
        self.horarios_disponibilidad = horarios_disponibilidad