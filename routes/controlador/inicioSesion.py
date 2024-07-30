# routes/controlador/inicioSesion.py
from flask import Blueprint, render_template, request, redirect, url_for, flash

inicio_sesion = Blueprint('inicio_sesion', __name__, template_folder='../templates/vista/HTML')

@inicio_sesion.route('/')
def login():
    return render_template('vista/assets/HTML/login.html')

@inicio_sesion.route('/registrarse')
def register_nav():
    return redirect(url_for('registrarse.register'))