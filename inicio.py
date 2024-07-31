import os
from flask import Flask, send_from_directory
from routes.controlador.home import home
from routes.controlador.perfil import perfil
from routes.controlador.inicioSesion import inicio_sesion
from routes.controlador.registrarse import registrarse
from routes.controlador.administrador import administrador
from routes.controlador.autor import autor
from utils.repositorios.sqlAlchemy.conexionBd import db
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mi_clave_secreta_super_segura'

db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')

# Configurar la URI de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{db_user}:{db_password}@{db_host}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.register_blueprint(registrarse, url_prefix='/registrarse')
app.register_blueprint(inicio_sesion, url_prefix='/login')
app.register_blueprint(administrador, url_prefix='/admin')
app.register_blueprint(autor, url_prefix='/autor')
app.register_blueprint(home, url_prefix='/')
app.register_blueprint(perfil, url_prefix='/perfil')


@app.route('/templates/vista/assets/CSS/<path:filename>')
def custom_static(filename):
    return send_from_directory('templates/vista/assets/CSS', filename)

if __name__ == '__main__':
    app.run(debug=True)
