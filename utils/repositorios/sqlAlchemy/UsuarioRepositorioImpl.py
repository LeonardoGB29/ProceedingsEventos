#!/usr/bin/python
#-*- coding: utf-8 -*-

from utils.repositorios.sqlAlchemy.conexionBd import db

def agregar_usuario_bd(usuario):
    db.session.add(usuario)
    db.session.commit()


class UsuarioRepositorioImpl():
    pass
