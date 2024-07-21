from flask import Blueprint, render_template

perfil = Blueprint('perfil', __name__,template_folder='../Assets/HTML')

@perfil.route('/home/perfil')
def home():
    return render_template('perfil.html')