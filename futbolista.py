# -*- coding: utf-8 -*-
from deportista import Deportista
from persona import Persona

class Futbolista(Persona, Deportista):
    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, añosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        
    def setGolesMarcados(self,x):
         self._golesMarcados = x    
    def getGolesMarcados(self):
        return self._golesMarcados
    def setTarjetasRojas(self,x):
       self._tarjetasRojas = x
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    def setPiernaHabil(self,x):
        self._piernaHabil = x
    def getPiernaHabil(self):
        return self._piernaHabil
    
    def __str__(self):
        return "Mi nombre es "+self.getNombre()+" soy profesional en el deporte "+self.getDeporte()+" Tengo "+str(self.getEdad())+" años de edad y llevo "+str(self.getAñosPracticando())+" años en el deporte"