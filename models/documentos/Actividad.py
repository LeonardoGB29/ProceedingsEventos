from utils.repositorios.sqlAlchemy.conexionBd import db

class Actividad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    descripcion = db.Column(db.String(100))
    autores = db.Column(db.String(100))
    responsables = db.Column(db.String(100))

    def __init__(self, nombre, descripcion, autores, responsables):
        self.nombre = nombre
        self.descripcion = descripcion
        self.autores = autores
        self.responsables = responsables