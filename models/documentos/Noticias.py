from utils.repositorios.sqlAlchemy.conexionBd import db

class Noticias(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    contenido = db.Column(db.Text)
    fecha = db.Column(db.Date)

    def __init__(self, titulo, contenido, fecha):
        self.titulo = titulo
        self.contenido = contenido
        self.fecha = fecha