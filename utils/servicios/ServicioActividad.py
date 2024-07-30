from utils.repositorios.sqlAlchemy.ActividadRepositorioImpl import agregar_actividad
from utils.repositorios.sqlAlchemy.conexionBd import db

def registrar_actividad(actividad):
    agregar_actividad(actividad)
    return "guardando actividad"