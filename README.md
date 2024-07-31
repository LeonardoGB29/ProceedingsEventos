# ProcedingsEventos

# LAB 9

# Prácticas Aplicadas

# Nombres

Se utiliza nombres coherentes y descriptivos para funciones y variables

@registrarse.route('/enviarRegistro', methods=['POST'])
def registro():
    nombres = request.form['nombres']
    apellidos = request.form['apellidos']
    email = request.form['email']
    contrasenia = request.form['contrasenia']

    nuevo_usuario = Usuario(nombres, apellidos, email, contrasenia)

    # Verificar si el usuario ya existe
    if registrar_usuario(nuevo_usuario):
        return redirect(url_for('inicio_sesion.login'))
    else:
        flash('El usuario ya existe')
        return redirect(url_for('registrarse.register'))

#### Funciones

Tenemos la funcion registrar_usuario que verifica en la base de datos si el usuario esta registrado y si no, lo agrega.

def registrar_usuario(usuario):
    
    if not verificar_usuario_bd(usuario):
        return False
    
    agregar_usuario_bd(usuario)
    return True


# Estructura de Código Fuente

Se mantiene la estructura de un proyecto en Flask, mantendiendo la arquitectura propuesta.

# LAB 10

# Single-responsibility principle (SRP)

Se dividió el código en funciones modulares.

def registrar_usuario(usuario):
    
    if not verificar_usuario_bd(usuario):
        return False
    
    agregar_usuario_bd(usuario)
    return True

En ServicioUsuario tenemos la funcion registrar usuario que usa otra funcion verificar_usuario_bd, donde solo hace la consulta en la base de datos, y en el servicio esta la logica.

def verificar_usuario_bd(usuario):
    usuario_db = db.session.query(Usuario).filter_by(nombres=usuario.nombres, apellidos=usuario.apellidos, email=usuario.email).first()
    return usuario_db is None

# Open-closed principle (OCP)

Flask nos permite el uso de blueprints, asi podemos agregar mas rutas sin la necesidad de cambiar los otros archivos

app.register_blueprint(registrarse, url_prefix='/registrarse')
app.register_blueprint(inicio_sesion, url_prefix='/login')
app.register_blueprint(administrador, url_prefix='/admin')
app.register_blueprint(autor, url_prefix='/autor')
app.register_blueprint(home, url_prefix='/')

# Dependency inversion principle (DIP)

Vemos que solo tenemos una instancia de la base de datos, y lo unico que pasamos es una clase, asi que podemos usar otra base de datos solo modificando este codigo

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from utils.repositorios.sqlAlchemy.conexionBd import db
from models.entidades.Usuario import Usuario

def agregar_usuario_bd(usuario):
    db.session.add(usuario)
    db.session.commit()

def verificar_usuario_bd(usuario):
    usuario_db = db.session.query(Usuario).filter_by(nombres=usuario.nombres, apellidos=usuario.apellidos, email=usuario.email).first()
    return usuario_db is None


# LAB 11

# Error/Exception Handling

@registrarse.route('/enviarRegistro', methods=['POST'])
def registro():
    try:
        nombres = request.form['nombres'].strip()
        apellidos = request.form['apellidos'].strip()
        email = request.form['email'].strip()
        contrasenia = request.form['contrasenia'].strip()
        
        ...

        nuevo_usuario = Usuario(nombres, apellidos, email, contrasenia)

        if registrar_usuario(nuevo_usuario):
            flash('Registro exitoso, por favor inicie sesión.')
            return redirect(url_for('inicio_sesion.login'))
        else:
            flash('El usuario ya existe.')
            return redirect(url_for('registrarse.home_register'))

    except Exception as e:

        flash(f'Ocurrió un error: {str(e)}')
        return redirect(url_for('registrarse.home_register'))

# Things

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(80))
    apellidos = db.Column(db.String(80))
    email = db.Column(db.String(120))
    contrasenia = db.Column(db.String(120))

    def __init__(self, nombres, apellidos, email,contrasenia):
        self.nombres = nombres
        self.apellidos = apellidos
        self.email = email
        self.contrasenia = contrasenia

    def registrarse_evento(cls):
        return
    
# Cookbook

La base de datos se comporta como un singleton

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

