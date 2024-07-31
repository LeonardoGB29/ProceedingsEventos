# models/documentos/Evento.py
from utils.repositorios.sqlAlchemy.conexionBd import db

class Evento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))  # Ajusta el tamaño según sea necesario
    descripcion = db.Column(db.String(100))
    autores = db.Column(db.String(100))
    responsables = db.Column(db.String(100))

    def __init__(self, nombre, descripcion, autores, responsables):
        self.nombre = nombre
        self.descripcion = descripcion
        self.autores = autores
        self.responsables = responsables

    def mostrar_evento(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "autores": self.autores,
            "responsables": self.responsables
        }
