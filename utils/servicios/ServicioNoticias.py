from utils.repositorios.sqlAlchemy.NoticiasRepositorioImpl import agregar_noticias
from utils.repositorios.sqlAlchemy.conexionBd import db

def registrar_noticias(noticia):
    agregar_noticias(noticia)
    return "guardando noticia"