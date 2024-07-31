# routes/controlador/inicioSesion.py
from flask import Blueprint, render_template

inicio_sesion = Blueprint('inicio_sesion', __name__, template_folder='../templates/vista/HTML')

@inicio_sesion.route('/login')
def login():
    return render_template('vista/assets/HTML/login.html')