# Proyecto de Sistema de Publicación de Proceedings de Eventos

## Propósito del Proyecto
Este proyecto tiene como objetivo desarrollar un sistema de publicación de proceedings de eventos académicos. La plataforma integral facilitará la carga, revisión, publicación y acceso a los trabajos presentados en estos eventos, optimizando y agilizando los procesos involucrados.

## Funcionalidades
### Diagrama de Casos de Uso
![Diagrama de Casos de Uso](https://github.com/DanielfQo/ProceedingsEventos/edit/desarrollo/diagrama.png)

### Funcionalidades de Alto Nivel
- **Registrar Usuarios:** Permitir el registro de nuevos usuarios en el sistema.
- **Ver Eventos:** Mostrar eventos disponibles a los usuarios.
- **Agregar Evento:** Permitir a los administradores crear nuevos eventos.
- **Definir Cronograma:** Establecer fechas y horarios para los eventos.
- **Enviar Paper:** Facilitar el envío de papers para revisión.

### Prototipo (o GUI)
- **Vista:** 
  - crear_evento.html
  - subir_documento.html
  - home.html
  - login.html
  - perfil.html
  - registro.html

## Modelo de Dominio
### Diagrama de Clases y Módulos
![Diagrama de Clases](https://github.com/DanielfQo/ProceedingsEventos/edit/desarrollo/diagramaClases.png)

## Arquitectura y Patrones
### Diagrama de Componentes o Paquetes
![Diagrama de Componentes](https://github.com/DanielfQo/ProceedingsEventos/edit/desarrollo/diagramaComponentes.png)

## Prácticas de Codificación Limpia Aplicadas
### Descripción y Fragmento de Código (evidencia)
Se utilizan nombres coherentes y descriptivos para funciones y variables.

```python
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
```


## Principios SOLID Aplicados
### Descripción y Fragmento de Código (evidencia)
### Single-responsibility principle (SRP):
El código se divide en funciones modulares.

```python
def registrar_usuario(usuario):
    if not verificar_usuario_bd(usuario):
        return False

    agregar_usuario_bd(usuario)
    return True
```
En ServicioUsuario tenemos la función registrar_usuario que usa otra función verificar_usuario_bd, donde solo se hace la consulta en la base de datos, y en el servicio está la lógica.

```python
def verificar_usuario_bd(usuario):
    usuario_db = db.session.query(Usuario).filter_by(nombres=usuario.nombres, apellidos=usuario.apellidos, email=usuario.email).first()
    return usuario_db is None
```

### Open-closed principle (OCP):
Flask permite el uso de blueprints, así podemos agregar más rutas sin la necesidad de cambiar los otros archivos.

```python
app.register_blueprint(registrarse, url_prefix='/registrarse')
app.register_blueprint(inicio_sesion, url_prefix='/login')
app.register_blueprint(administrador, url_prefix='/admin')
app.register_blueprint(autor, url_prefix='/autor')
app.register_blueprint(home, url_prefix='/')
```
### Dependency inversion principle (DIP):
Tenemos una instancia de la base de datos y solo pasamos una clase, lo que permite usar otra base de datos solo modificando este código.

```python
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
```

## Conceptos DDD Aplicados
### Descripción y Fragmento de Código (evidencia)
#### Entidades:

```python
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(80))
    apellidos = db.Column(db.String(80))
    email = db.Column(db.String(120))
    contrasenia = db.Column(db.String(120))

    def __init__(self, nombres, apellidos, email, contrasenia):
        self.nombres = nombres
        self.apellidos = apellidos
        self.email = email
        self.contrasenia = contrasenia
```

#### Servicios de Dominio:

```python
def registrar_usuario(usuario):
    if not verificar_usuario_bd(usuario):
        return False

    agregar_usuario_bd(usuario)
    return True
```    
#### Repositorios:

```python
def agregar_usuario_bd(usuario):
    db.session.add(usuario)
    db.session.commit()

def verificar_usuario_bd(usuario):
    usuario_db = db.session.query(Usuario).filter_by(nombres=usuario.nombres, apellidos=usuario.apellidos, email=usuario.email).first()
    return usuario_db is None
```
    
#### Arquitectura en Capas:
El sistema sigue una arquitectura en capas que incluye Presentación, Servicios, Dominio y Repositorios, asegurando una separación clara de responsabilidades y facilitando el mantenimiento y escalabilidad del sistema.
