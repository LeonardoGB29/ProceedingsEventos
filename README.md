# Laboratorio 11: Estilos de Programación
# Estilos de Programación Implementados
## Error/Exception Handling
Implementé el manejo de errores y excepciones para gestionar fallos en las operaciones de la base de datos, aumentando la robustez de la aplicación.
**Ejemplo:**
```python
try:
    db.session.add(nuevo_documento)
    db.session.commit()
except Exception as e:
    db.session.rollback()
    raise e
```
## Persistent-Tables
Aseguré que todas las operaciones con la base de datos se manejen coherentemente usando transacciones, encapsulando estas operaciones dentro de los modelos.
```python
@staticmethod
def crear_documento(resumen, datos, conclusion, num_pag, evento_id):
    try:
        nuevo_documento = Documento(resumen, datos, conclusion, num_pag, evento_id)
        db.session.add(nuevo_documento)
        db.session.commit()
        return nuevo_documento
    except Exception as e:
        db.session.rollback()
        raise e
```

## Trinity (MVC)
Aplicando el patrón Trinity (Modelo-Vista-Controlador), separé las responsabilidades entre Modelos, Vistas y Controladores para mejorar la modularidad y mantenibilidad del proyecto. Los Modelos gestionan la lógica de negocio y la interacción con la base de datos, las Vistas se encargan de la presentación y los Controladores manejan las solicitudes del usuario, delegando la lógica de negocio a los Modelos.
Aplicando el patrón Trinity (Modelo-Vista-Controlador), separé las responsabilidades entre Modelos, Vistas y Controladores para mejorar la modularidad y mantenibilidad del proyecto. Los Modelos gestionan la lógica de negocio y la interacción con la base de datos usando SQLAlchemy, las Vistas se encargan de la presentación y los Controladores manejan las solicitudes del usuario. 
