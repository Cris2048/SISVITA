from utils.db import db
from models.tests import Tests


class Preguntas(db.Model):
    __tablename__ = 'Preguntas'
    
    pregunta_id = db.Column(db.Integer, primary_key=True)
    test_id = db.Column(db.Integer, db.ForeignKey('Tests.test_id'), nullable=True)
    texto_pregunta = db.Column(db.Text, nullable=False)

    def __init__(self, pregunta_id, test_id, texto_pregunta):
        self.pregunta_id = pregunta_id
        self.test_id = test_id
        self.texto_pregunta = texto_pregunta