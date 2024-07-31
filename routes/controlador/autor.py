from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.documentos.Documento import Documento
from models.documentos.Evento import Evento

autor = Blueprint('autor', __name__, template_folder='../templates/vista/HTML')

@autor.route('/subir_documento', methods=['POST'])
def subir_documento():
    try:
        resumen = request.form['resumen']
        datos = request.form['datos']
        conclusion = request.form['conclusion']
        num_pag = request.form['num_pag']
        evento_id = request.form['evento_id']
        nuevo_documento = Documento.crear_documento(resumen, datos, conclusion, num_pag, evento_id)
        flash('Documento subido exitosamente', 'success')
    except Exception as e:
        flash(f'Error al subir el documento: {str(e)}', 'error')
    return redirect(url_for('autor.subir_documento_form'))

@autor.route('/subir_documento_form', methods=['GET'])
def subir_documento_form():
    try:
        eventos = Evento.query.all()
        return render_template('vista/assets/HTML/subir_documento.html', eventos=eventos)
    except Exception as e:
        flash(f'Error al cargar el formulario: {str(e)}', 'error')
        return redirect(url_for('autor.subir_documento_form'))
