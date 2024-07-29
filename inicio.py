from flask import Flask, send_from_directory
from routes.controlador.inicioSesion import inicio_sesion
from routes.controlador.registrarse import registrarse
from utils.repositorios.sqlAlchemy.conexionBd import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:leogb29@127.0.0.1/proceedingsEventos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(registrarse, url_prefix='/')
app.register_blueprint(inicio_sesion, url_prefix='/login')

# ruta css???
@app.route('/templates/vista/assets/CSS/<path:filename>')
def custom_static(filename):
    return send_from_directory('templates/vista/assets/CSS', filename)
