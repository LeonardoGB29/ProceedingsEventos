from flask import Flask
from .Vista.Routes.inicioSesion import inicioSesion

app = Flask(__name__)

app.register_blueprint(inicioSesion)

