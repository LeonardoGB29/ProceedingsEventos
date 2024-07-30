from models.entidades.Usuario import Usuario
from utils.repositorios.sqlAlchemy.conexionBd import db

class Administrador(Usuario):
    id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)

    def __init__(self, nombres, apellidos, email, contrasenia):
        super().__init__(nombres, apellidos, email, contrasenia)

    def crear_evento(self, evento):
        pass

    def actualizar_evento(self, evento):
        pass
