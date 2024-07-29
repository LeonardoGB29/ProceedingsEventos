from utils.repositorios.sqlAlchemy.UsuarioRepositorioImpl import agregar_usuario_bd
from utils.repositorios.sqlAlchemy.conexionBd import db

def registrar_usuario(usuario):
    agregar_usuario_bd(usuario)

    return "guardando usuario"