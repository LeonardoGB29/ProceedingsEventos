from utils.repositorios.sqlAlchemy.conexionBd import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombres = db.Column(db.String(80))
    apellidos = db.Column(db.String(80))
    email = db.Column(db.String(120))
    fecha_nacimiento = db.Column(db.Date)
    nacionalidad = db.Column(db.String(120))
    contrasenia = db.Column(db.String(255))

    def __init__(self, nombres, apellidos, email,contrasenia):
        self.nombres = nombres
        self.apellidos = apellidos
        self.email = email
        self.contrasenia = contrasenia
<<<<<<< HEAD

    def registrarse_evento(cls):
        return
    
=======
    
    @classmethod
    def buscar_por_email(cls, email):
        return cls.query.filter_by(email=email).first()
    
    def verificar_contrasenia(self, contrasenia):
        return self.contrasenia == contrasenia
>>>>>>> 366c41f91baf0e2551f251ddded71252ba5c5df0
