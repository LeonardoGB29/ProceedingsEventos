#!/usr/bin/python
#-*- coding: utf-8 -*-


from utils.servicios.ServicioUsuario import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombres = db.Column(db.String(80))
    apellidos = db.Column(db.String(80))
    email = db.Column(db.String(120))
    #fecha_nacimiento = db.Column(db.Date)
    #nacionalidad = db.Column(db.String(120))

    #contrasenia = db.Column(db.String(120))

    def __init__(self, nombre, apellidos, email): #, fecha_nacimiento, nacionalidad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        #self.fecha_nacimiento = fecha_nacimiento
        #self.nacionalidad = nacionalidad
        
        #self.contrasenia = contrasenia