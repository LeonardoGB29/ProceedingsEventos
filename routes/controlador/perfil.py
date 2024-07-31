from flask import Blueprint, render_template, session, redirect, url_for
from models.entidades.Usuario import Usuario

perfil = Blueprint('perfil', __name__)

@perfil.route('/')
def mostrar_perfil():
    if 'usuario_id' not in session:
        return redirect(url_for('inicio_sesion_bp.login'))
    
    usuario_id = session['usuario_id']
    usuario = Usuario.query.get(usuario_id)
    
    if usuario:
        return render_template('vista/assets/HTML/perfil.html', usuario=usuario)
    else:
        return "Usuario no encontrado", 404
