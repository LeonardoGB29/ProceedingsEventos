#!/usr/bin/python
#-*- coding: utf-8 -*-

from utils.repositorios.sqlAlchemy.conexionBd import db
from models.entidades.Usuario import Usuario

def agregar_usuario_bd(usuario):
    db.session.add(usuario)
    db.session.commit()

def verificar_usuario_bd(usuario):
    usuario_db = db.session.query(Usuario).filter_by(nombres=usuario.nombres, apellidos=usuario.apellidos, email=usuario.email).first()
    return usuario_db is None

