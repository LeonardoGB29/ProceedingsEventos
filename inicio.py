from flask import Flask
from routes.controlador.inicioSesion import inicioSesion
from routes.controlador.registrarse import registrarse
from utils.repositorios.sqlAlchemy.conexionBd import db
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://daniel:2004@localhost/proceedingsEventos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.register_blueprint(registrarse)