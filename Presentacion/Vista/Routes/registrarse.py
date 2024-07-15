from flask import Blueprint, render_template

registrarse = Blueprint('registrarse', __name__,template_folder='../Assets/HTML')

@registrarse.route('/registro')
def home():
    return render_template('registro.html')