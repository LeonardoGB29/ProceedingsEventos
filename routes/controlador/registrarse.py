from flask import Blueprint, render_template, request
from models.entidades.Usuario import Usuario
from utils.servicios.ServicioUsuario import registrar_usuario


registrarse = Blueprint('registrarse', __name__, template_folder='')

@registrarse.route('/')
def home():
    return render_template('vista/assets/HTML/registro.html')

@registrarse.route('/registrarse', methods=['POST'])
def registro():
    nombres = request.form['nombres']
    apellidos = request.form['apellidos']
    email = request.form['email']
    contrasenia = request.form['contrasenia']

    nuevo_usuario = Usuario(nombres, apellidos, email, contrasenia)

    registrar_usuario(nuevo_usuario)

    return 'Usuario registrado'