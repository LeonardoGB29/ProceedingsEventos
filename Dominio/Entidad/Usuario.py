#!/usr/bin/python
#-*- coding: utf-8 -*-

from Dominio.Entidad.Administrador import Administrador
from Dominio.Entidad.Autor import Autor

class Usuario(Administrador, Autor):
    def __init__(self):
        self.nombre = None
        self.email = None
        self.id = None

    def registrarse(self, ):
        pass

