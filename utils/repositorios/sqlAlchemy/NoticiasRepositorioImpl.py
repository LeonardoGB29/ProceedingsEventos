from utils.repositorios.sqlAlchemy.conexionBd import db
from models.documentos.Noticias import Noticias

def agregar_noticias(noticia):
    db.session.add(noticia)
    db.session.commit()

class NoticiasRepositorioImpl: