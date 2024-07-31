from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.entidades.Usuario import Usuario
from utils.servicios.ServicioUsuario import registrar_usuario
from utils.repositorios.sqlAlchemy.conexionBd import db
from werkzeug.security import generate_password_hash

registrarse = Blueprint('registrarse', __name__, template_folder='../templates/vista/HTML')

@registrarse.route('/')
def register():
    return render_template('vista/assets/HTML/registro.html')

@registrarse.route('/enviarRegistro', methods=['POST'])
def registro():
    nombres = request.form['nombres']
    apellidos = request.form['apellidos']
    email = request.form['email']
    contrasenia = generate_password_hash(request.form['contrasenia'])

    nuevo_usuario = Usuario(nombres=nombres, apellidos=apellidos, email=email, contrasenia=contrasenia)

    if registrar_usuario(nuevo_usuario):
        session['usuario_id'] = nuevo_usuario.id
        return redirect(url_for('home.home_page'))
    else:
        flash('El usuario ya existe')
        return redirect(url_for('registrarse.register'))
