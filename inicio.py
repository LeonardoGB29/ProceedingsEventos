from flask import Flask
from routes.controlador.inicioSesion import inicioSesion
from routes.controlador.registrarse import registrarse
from utils.servicios.ServicioUsuario import db
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost/proceedingsEventos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.register_blueprint(registrarse)