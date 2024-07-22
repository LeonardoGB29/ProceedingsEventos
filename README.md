# ProceedingsEventos

# Laboratorio 9(CLEAN CODE)
Practicas Aplicadas
1. Uso Consistente de Estilo

Se usa adecuadamente las convenciones del estilo del lenguaje(PEP 8), por ejemplo en las clases del dominio, como nombres, atributos y sus metodos

2. Funciones Pequeñas y Concisas

Funciones dentro de registrarse.py, son entendibles y cada una hace cosas diferentes.
```python

@perfil_bp.route('/perfil/<int:usuario_id>')
def mostrar_perfil(usuario_id):
    usuario = Usuario.query.get(usuario_id)
    if usuario:
        return render_template('perfil.html', usuario=usuario)
    else:
        return "Usuario no encontrado", 404

```
## Conflictos
1. hay un conflicto al querer mostrar los datos de la base de datos 


# Laboratorio 10(SOLID)

1. Single-responsibility principle (SRP)

Cada modulo y clase en nuestro proyecto tiene una unica responsabilidad. Por ejemplo, index.py se encarga solo de cargar el proyecto.

2. Open-closed principle (OCP)

Actualmente el codigo esta organizado para ser extendido sin modificar el codigo existente. Por ejemplo, al usar Blueprints en Flask, podemos agregar nuevas rutas sin modificar el codigo existente.