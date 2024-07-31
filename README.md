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
