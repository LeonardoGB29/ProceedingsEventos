# routes/controlador/registrarse.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.entidades.Usuario import Usuario
from utils.servicios.ServicioUsuario import registrar_usuario

registrarse = Blueprint('registrarse', __name__, template_folder='../templates/vista/HTML')

@registrarse.route('/')
def register():
    return render_template('vista/assets/HTML/registro.html')

@registrarse.route('/enviarRegistro', methods=['POST'])
def registro():
    nombres = request.form['nombres']
    apellidos = request.form['apellidos']
    email = request.form['email']
    contrasenia = request.form['contrasenia']

    nuevo_usuario = Usuario(nombres, apellidos, email, contrasenia)

    if registrar_usuario(nuevo_usuario):
        return redirect(url_for('inicio_sesion.login'))
    else:
        flash('El usuario ya existe')
        return redirect(url_for('registrarse.register'))
