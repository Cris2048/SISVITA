from utils.db import db
from models.preguntas import Preguntas



class Opciones(db.Model):
    __tablename__ = 'Opciones'
    
    opcion_id = db.Column(db.Integer, primary_key=True)
    pregunta_id = db.Column(db.Integer, db.ForeignKey('Preguntas.pregunta_id'), nullable=True)
    texto_opcion = db.Column(db.Text, nullable=True)
    es_correcta = db.Column(db.Boolean, nullable=True)

    def __init__(self, opcion_id, pregunta_id, texto_opcion, es_correcta):
        self.opcion_id = opcion_id
        self.pregunta_id = pregunta_id
        self.texto_opcion = texto_opcion
        self.es_correcta = es_correcta