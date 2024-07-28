from flask import Flask
from routes.controlador.inicioSesion import inicio_sesion
from routes.controlador.registrarse import registrarse
from utils.repositorios.sqlAlchemy.conexionBd import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:leogb29@127.0.0.1/proceedingsEventos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(registrarse, url_prefix='/')
app.register_blueprint(inicio_sesion, url_prefix='/login')
