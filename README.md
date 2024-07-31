github: https://github.com/KevinRodriguezLima/ProceedingsEventos
# LAB 9, 10 (ABAJO)

# LAB 11
# Acividad Laboratorio 11: Estilos de Programación

# Estilos aplicados
## Estilo de Programación: Things
Lo utilizo al encapsular datos y comportamientos en clases. Por ejemplo en models/Actividad.py : 

class Actividad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    descripcion = db.Column(db.String(100))
    autores = db.Column(db.String(100))
    responsables = db.Column(db.String(100))

    def __init__(self, nombre, descripcion, autores, responsables):
        self.nombre = nombre
        self.descripcion = descripcion
        self.autores = autores
        self.responsables = responsables

## Estilo de Programación: Persistent-Tables
Tambien se puede decir que he utilizado el estilo de programación Persistent-Tables para gestionar y modelar los datos mediante el uso de tablas, ejemplo en models/Noticias.py:

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

## Estilo de Programación: 
Respecto a lo que tenia que implementar no estoy utilizando otros estilos ya que me toco sobre todo modelado de tablas y hmtl asi como controladores, añadire más codigo o en otras secciones donde se pueda usar otros estilos.

# Acividad Laboratorio 9( CLEAN CODE )

# Prácticas Aplicadas

# Nombres

Se utilizo nombres coherentes y descriptivos para funciones y variables. Por ejemplo: 
@rutas.route('/')
def home():
    cronograma = Cronograma.query.all()
    noticias = Noticias.query.all()
    return render_template('inicio.html', cronograma=cronograma, noticias=noticias)

`def home`se encarga de manejar la lógica para mostrar la página de `inicio`, dentro de esta función se obtienen los datos necesarios (cronogramas y noticias) de la base de datos para poder mostrarlos en la interfaz de usuario.

#### Funciones

Se dividió el código en funciones pequeñas y enfocadas. Por ejemplo, la función `initialize_database` en `inicio.py` se encarga únicamente de inicializar la base de datos.

def initialize_database():
    with app.app_context():
        db.create_all()


#### Comentarios

Se agrego comentarios descriptivos  a funciones y rutas para mejorar la comprensión del código. Por ejemplo:

def create_app():
    
    #Función para crear y configurar la aplicación Flask
    app = Flask(__name__, template_folder='Vista/Assets/HTML')

    #Configuración para SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Promundial1?@localhost/cronogramadb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(rutas)

    return app

# Estructura de Código Fuente

Se mantuvo el orden que se planteo en laboratorios anteriores, el código en módulos y paquetes claros y coherentes, siguiendo las convenciones de estructura de proyectos de Flask aunque todabia hay muchas cosas por hacer y unir con las partes de mis compañeros.

# LAB 10

# Principios SOLID aplicados
# Single-responsibility principle (SRP)

Cada módulo y clase en nuestro proyecto tiene una única responsabilidad. Por ejemplo, create_app se encarga solo de crear y configurar la aplicación Flask, y initialize_database se encarga de inicializar la base de datos.
Tambien ServicioActividad.py se encarga exclusivamente de la lógica relacionada con las actividades: 

from utils.repositorios.sqlAlchemy.ActividadRepositorioImpl import agregar_actividad
from utils.repositorios.sqlAlchemy.conexionBd import db

def registrar_actividad(actividad):
    agregar_actividad(actividad)
    return "guardando actividad"


# Open-closed principle (OCP)

Actualmente el codigo esta organizado para ser extendido sin modificar el código existente. Por ejemplo, al usar Blueprints en Flask, podemos agregar nuevas rutas sin modificar el código existente:

app.register_blueprint(home, url_prefix='/')

Tambien hay archivos como cronograma.py, noticias.py que mantienen una separacion clara para poder definir y manipular la BD, si se deseara añadir nuevas tablas o configuraciones solo se crea mas archivos pero siempre dentro de Repositorios/SQLAlchemy..

# Dependency inversion principle (DIP)

Se puede decir qe utilizamos este principio al utilizar inyección de dependencias para la configuración y creación de la base de datos.
Ejemplo:

from utils.repositorios.sqlAlchemy.conexionBd import db


# Uso de SonarLint

SonarLint me arrojaba una vulnerabilidad que es debido a que la contraseña de mi base de datos estaba expuesta, con mi grupo optamos todos por usar variables de entorno y lo solucionamos ya que era un problema general.