from utils.repositorios.sqlAlchemy.conexionBd import db

class Evento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    edicion = db.Column(db.String(50), nullable=False)

    def __init__(self, nombre, fecha, edicion):
        self.nombre = nombre
        self.fecha = fecha
        self.edicion = edicion

    def mostrar_evento(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "fecha": self.fecha,
            "edicion": self.edicion
        }

    @staticmethod
    def crear_evento(nombre, fecha, edicion):
        try:
            nuevo_evento = Evento(nombre, fecha, edicion)
            db.session.add(nuevo_evento)
            db.session.commit()
            return nuevo_evento
        except Exception as e:
            db.session.rollback()
            raise e
