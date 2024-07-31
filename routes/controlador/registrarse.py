from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.entidades.Usuario import Usuario
from utils.servicios.ServicioUsuario import registrar_usuario

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
        contrasenia = request.form['contrasenia'].strip()
        

        if not (nombres and apellidos and email and contrasenia):
            flash('Todos los campos son requeridos.')
            return redirect(url_for('home_register'))
        

        if '@' not in email or '.' not in email:
            flash('El formato del email no es válido.')
            return redirect(url_for('home_register'))

        nuevo_usuario = Usuario(nombres, apellidos, email, contrasenia)

        if registrar_usuario(nuevo_usuario):
            flash('Registro exitoso, por favor inicie sesión.')
            return redirect(url_for('inicio_sesion.login'))
        else:
            flash('El usuario ya existe.')
            return redirect(url_for('registrarse.home_register'))

    except Exception as e:

        flash(f'Ocurrió un error: {str(e)}')
        return redirect(url_for('registrarse.home_register'))

