from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.documentos.Evento import Evento
from utils.repositorios.sqlAlchemy.conexionBd import db

administrador = Blueprint('administrador', __name__, template_folder='../templates/vista/HTML')

@administrador.route('/crear_evento', methods=['POST'])
def crear_evento():
    nombre = request.form['nombre']
    fecha = request.form['fecha']
    edicion = request.form['edicion']
    nuevo_evento = Evento(nombre, fecha, edicion)
    db.session.add(nuevo_evento)
    db.session.commit()
    flash('Evento creado exitosamente', 'success')
    return redirect(url_for('administrador.crear_evento'))

@administrador.route('/crear_evento_form', methods=['GET'])
def crear_evento_form():
    return render_template('vista/assets/HTML/crear_evento.html')


#@administrador.route('/actua_evento', methods=['GET', 'POST'])
#def actualizar_evento():