#!/usr/bin/python
#-*- coding: utf-8 -*-

# FabricaUsuario.py
from models.entidades.Usuario import Usuario
from werkzeug.security import generate_password_hash

class FabricaUsuario:
    @staticmethod
    def crear_usuario(nombres, apellidos, email, contrasenia):
        # Aquí puedes agregar lógica adicional, como validaciones o configuraciones por defecto
        contrasenia_hashed = generate_password_hash(contrasenia)
        return Usuario(nombres=nombres, apellidos=apellidos, email=email, contrasenia=contrasenia_hashed)
