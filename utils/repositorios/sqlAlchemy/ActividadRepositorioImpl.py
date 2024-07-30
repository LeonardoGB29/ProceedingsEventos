from utils.repositorios.sqlAlchemy.conexionBd import db
from models.documentos.Actividad import Actividad

def agregar_actividad(actividad):
    db.session.add(actividad)
    db.session.commit()

class ActividadRepositorioImpl:
    pass
