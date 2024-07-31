from utils.repositorios.sqlAlchemy.UsuarioRepositorioImpl import agregar_usuario_bd, verificar_usuario_bd
from utils.repositorios.sqlAlchemy.conexionBd import db

def registrar_usuario(usuario):
    
    if not verificar_usuario_bd(usuario):
        return False
    
    agregar_usuario_bd(usuario)
    return True

    