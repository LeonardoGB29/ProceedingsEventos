from utils.repositorios.sqlAlchemy.conexionBd import db
from models.documentos.Evento import evento

class EventoRepositorioImpl(evento):

    def agregar_evento(evento):
        db.session.add(evento)
        db.session.commit()
