from flask import Blueprint, render_template, request, redirect, url_for
from models.entidades.Usuario import Usuario
from utils.servicios.ServicioUsuario import db

perfil_bp = Blueprint('perfil', __name__)

@perfil_bp.route('/perfil/<int:usuario_id>')
def mostrar_perfil(usuario_id):
    usuario = Usuario.query.get(usuario_id)
    if usuario:
        return render_template('perfil.html', usuario=usuario)
    else:
        return "Usuario no encontrado", 404

