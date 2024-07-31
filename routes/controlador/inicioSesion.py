# routes/controlador/inicioSesion.py
from flask import Blueprint, render_template, request, redirect, url_for, session
from models.entidades.Usuario import Usuario
from utils.repositorios.sqlAlchemy.conexionBd import db
from werkzeug.security import check_password_hash

inicio_sesion = Blueprint('inicio_sesion', __name__, template_folder='../templates/vista/HTML')


@inicio_sesion.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        contrasenia = request.form['contrasenia']

        usuario = Usuario.query.filter_by(email=email).first()

        if usuario and check_password_hash(usuario.contrasenia, contrasenia):
            session['usuario_id'] = usuario.id
            return redirect(url_for('home.home_page'))

    return render_template('vista/assets/HTML/login.html')