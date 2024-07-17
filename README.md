# Laboratorio 9: CLEAN CODE

## Nombres Claros y Descriptivos
En este proyecto, nos hemos enfocado en utilizar nombres claros y descriptivos para funciones y variables, lo cual es esencial para mantener el código comprensible y mantenible. Las rutas en nuestro servidor Flask son un buen ejemplo de esta práctica, facilitando la comprensión rápida de qué datos se están manejando y qué se retorna.

## Estructura de Base de Datos Consistente
Además, hemos mantenido una estructura coherente con el modelado inicial para la construcción de la base de datos, asegurando que las modificaciones y mantenimiento futuro se realicen sin contratiempos.

## Funciones Concisas y Enfocadas
El código se ha organizado en funciones pequeñas y enfocadas, cada una con una responsabilidad clara. Por ejemplo, tenemos una función específica dedicada exclusivamente a la inicialización de la base de datos.

## Comentarios Descriptivos
Se agregaron comentarios descriptivos a las funciones y rutas para mejorar la comprensión del código y facilitar la colaboración entre desarrolladores. Estos comentarios ayudan a explicar la lógica y las decisiones detrás del código.

# Laboratorio 10: SOLID

## Uso de SonarLint
Durante el desarrollo, utilizamos SonarLint para identificar y resolver vulnerabilidades relacionadas con nuestra conexión a MySQL, además de atender diversas advertencias generadas por el uso de prácticas menos óptimas.

## Principios SOLID Implementados

### Dependency Inversion Principle (DIP)
Hemos aplicado el principio de Inversión de Dependencias para reducir la dependencia entre los módulos de alto nivel y los de bajo nivel mediante el uso de abstracciones.

### Single-Responsibility Principle (SRP)
Cada clase en nuestro proyecto tiene una sola responsabilidad y razón para cambiar, lo que simplifica la gestión del código.

### Intento de Implementar el Open-Closed Principle (OCP)
También hemos intentado implementar el principio de Abierto-Cerrado, donde las entidades deben estar abiertas para la extensión, pero cerradas para la modificación, aunque esto sigue siendo un trabajo en progreso.
