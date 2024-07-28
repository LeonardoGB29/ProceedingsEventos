from utils.repositorios.sqlAlchemy.EventoRepositorioImpl import agregar_evento
from utils.repositorios.sqlAlchemy.conexionBd import db

def registrar_evento(evento):
    agregar_evento(evento)

    return "guardando evento"
