# -*- coding: utf-8 -*-

class Deportista():
    def __init__(self, añosPracticando, deporte = "Futbol"):
        self._deporte = deporte
        self._añosPracticando = añosPracticando

    def setAñosPracticando(self, x):
        self._añosPracticando = x
    def getAñosPracticando(self):
        return self._añosPracticando 
    def setDeporte(self, x):
        self._deporte = x
    def getDeporte(self):
        return self._deporte
    