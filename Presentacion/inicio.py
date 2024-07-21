from flask import Flask
from .Vista.Routes.perfil import perfil

app = Flask(__name__)

app.register_blueprint(perfil)


