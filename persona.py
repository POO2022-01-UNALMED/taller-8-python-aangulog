# -*- coding: utf-8 -*-

class Persona():
    def __init__(self, nombre, edad, altura, sexo):
        self._nombre = nombre
        self._edad = edad
        self._altura = altura
        self._sexo = sexo
    
    def setNombre(self, x):
        self._nombre= x
    def getNombre(self):
        return self._nombre
    def setEdad(self, x):
        self._edad = x
    def getEdad(self):
        return self._edad
    def setAltura(self, x):
        self._altura = x
    def getAltura(self):
        return self._altura
    def setSexo(self, x):
        self._sexo = x
    def getSexo(self):
        return self._sexo