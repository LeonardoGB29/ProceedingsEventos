from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.documentos.Evento import Evento

administrador = Blueprint('administrador', __name__, template_folder='../templates/vista/HTML')

@administrador.route('/crear_evento', methods=['POST'])
def crear_evento():
    try:
        nombre = request.form['nombre']
        fecha = request.form['fecha']
        edicion = request.form['edicion']
        nuevo_evento = Evento.crear_evento(nombre, fecha, edicion)
        flash('Evento creado exitosamente', 'success')
    except Exception as e:
        flash(f'Error al crear el evento: {str(e)}', 'error')
    return redirect(url_for('administrador.crear_evento_form'))

@administrador.route('/crear_evento_form', methods=['GET'])
def crear_evento_form():
    return render_template('vista/assets/HTML/crear_evento.html')
    

#@administrador.route('/actua_evento', methods=['GET', 'POST'])
#def actualizar_evento():