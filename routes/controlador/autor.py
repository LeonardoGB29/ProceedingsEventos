from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.documentos.Documento import Documento
from models.documentos.Evento import Evento
from models.entidades.Autor import Autor
from utils.repositorios.sqlAlchemy.conexionBd import db

autor = Blueprint('autor', __name__, template_folder='../templates/vista/HTML')

@autor.route('/subir_documento', methods=['GET'])
def subir_documento_form():
    eventos = Evento.query.all()
    return render_template('vista/assets/HTML/subir_documento.html', eventos=eventos)

@autor.route('/subir_documento', methods=['POST'])
def subir_documento():
    resumen = request.form['resumen']
    datos = request.form['datos']
    conclusion = request.form['conclusion']
    num_pag = request.form['num_pag']
    evento_id = request.form['evento_id']
    nuevo_documento = Documento(resumen, datos, conclusion, num_pag, evento_id)
    db.session.add(nuevo_documento)
    db.session.commit()
    flash('Documento subido exitosamente', 'success')
    return redirect(url_for('autor.subir_documento_form'))
