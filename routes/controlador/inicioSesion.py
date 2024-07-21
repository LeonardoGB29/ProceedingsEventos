# routes/controlador/inicioSesion.py
from flask import Blueprint, render_template

inicio_sesion = Blueprint('inicioSesion', __name__, template_folder='')

@inicio_sesion.route('/login')
def login():
    return render_template('vista/assets/HTML/login.html')
