# ProcedingsEventos

github: https://github.com/KevinRodriguezLima/ProceedingsEventos
# LAB 9 Y 10(ABAJO)

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

# Open-closed principle (OCP)

Actualmente el codigo esta organizado para ser extendido sin modificar el código existente. Por ejemplo, al usar Blueprints en Flask, podemos agregar nuevas rutas sin modificar el código existente, tambien hay archivos como cronograma.py, noticias.py que mantienen una separacion clara para poder definir y manipular la BD, si se deseara añadir nuevas tablas o configuraciones solo se crea mas archivos pero siempre dentro de Repositorios/SQLAlchemy..

# Dependency inversion principle (DIP)

Se puede decir qe utilizamos este principio al utilizar inyección de dependencias para la configuración y creación de la base de datos.

# Uso de SonarLint

SonarLint me arroja una vulnerabilidad que es debido a que la contraseña de mi base de datos esta expuesta, me sugirio otra opcion pero la cual todavia no entendi, estoy trabajando para cambiarlo y que sea secreta.