from utils.repositorios.sqlAlchemy.conexionBd import db
from models.documentos.Evento import Evento

def agregar_evento(evento):
    db.session.add(evento)
    db.session.commit()

class EventoRepositorioImpl():
    pass
