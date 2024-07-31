from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.entidades.Usuario import Usuario
from utils.servicios.ServicioUsuario import registrar_usuario
from utils.repositorios.sqlAlchemy.conexionBd import db
from werkzeug.security import generate_password_hash

registrarse = Blueprint('registrarse', __name__, template_folder='../templates/vista/HTML')

@registrarse.route('/')
def home_register():
    return render_template('vista/assets/HTML/registro.html')

@registrarse.route('/enviarRegistro', methods=['POST'])
def registro():
    try:
        nombres = request.form['nombres'].strip()
        apellidos = request.form['apellidos'].strip()
        email = request.form['email'].strip()
        contrasenia = generate_password_hash(request.form['contrasenia'].strip())
        

        if not (nombres and apellidos and email and contrasenia):
            flash('Todos los campos son requeridos.')
            return redirect(url_for('home_register'))
        

        if '@' not in email or '.' not in email:
            flash('El formato del email no es válido.')
            return redirect(url_for('home_register'))

        nuevo_usuario = Usuario(nombres, apellidos, email, contrasenia)

        if registrar_usuario(nuevo_usuario):
            session['usuario_id'] = nuevo_usuario.id
            return redirect(url_for('home.home_page'))
        else:
            flash('El usuario ya existe')
            return redirect(url_for('registrarse.register'))

    except Exception as e:

        flash(f'Ocurrió un error: {str(e)}')
        return redirect(url_for('registrarse.home_register'))

