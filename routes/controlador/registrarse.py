# registrarse.py
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from utils.servicios.ServicioUsuario import registrar_usuario
from utils.repositorios.sqlAlchemy.conexionBd import db

from models.entidades.FabricaUsuario import FabricaUsuario  # Importa la fábrica

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

    # Usa la fábrica para crear el usuario
    nuevo_usuario = FabricaUsuario.crear_usuario(nombres, apellidos, email, contrasenia)

    if registrar_usuario(nuevo_usuario):
        session['usuario_id'] = nuevo_usuario.id
        return redirect(url_for('home.home_page'))
    else:
        flash('El usuario ya existe')
        return redirect(url_for('registrarse.register'))
