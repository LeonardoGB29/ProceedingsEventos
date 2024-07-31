from utils.repositorios.sqlAlchemy.conexionBd import db

class Autor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    documentos = db.Column(db.String(80), nullable=True) #relationship?

    def subir_documento(self, documento):
        self.documentos.append(documento)
        db.session.commit()

    def editar_documento(self, documento, nuevos_datos):
        documento.datos = nuevos_datos
        db.session.commit()
