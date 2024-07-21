#!/usr/bin/python
#-*- coding: utf-8 -*-


from utils.repositorios.sqlAlchemy.conexionBd import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(80))
    apellidos = db.Column(db.String(80))
    email = db.Column(db.String(120))
    contrasenia = db.Column(db.String(120))

    def __init__(self, nombres, apellidos, email,contrasenia):
        self.nombres = nombres
        self.apellidos = apellidos
        self.email = email
        self.contrasenia = contrasenia