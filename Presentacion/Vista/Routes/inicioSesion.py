from flask import Blueprint, render_template

inicioSesion = Blueprint('inicioSesion', __name__,template_folder='../Assets/HTML')

@inicioSesion.route('/')
def home():
    return render_template('inicioSesion.html')