# 1. Crea una clase llamada Persona que tenga:
# Un atributo nombre
# Un atributo edad
# Un métodito saludar() que muestre por pantalla:
# Hola, me llamo <nombre> y tengo <edad> años

class Persona():
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def saludar(self):
        print("Hola, me llamo",self.__nombre,"y tengo",self.__edad,"años")

persona1 = Persona("Francisco Lozano", 27)
persona1.saludar()