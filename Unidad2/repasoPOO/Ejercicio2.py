# Modifica la clase Persona para que:
# Tenga un métodito cumplir_anios() que:
# Sume 1 a la edad
# Muestre por pantalla:
# Ahora tengo <edad> años
#
# Desde el programa principal:
# Llama primero a saludar()
# Luego a cumplir_anios()
# Y otra vez a saludar()

class Persona():
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def saludar(self):
        print("Hola, me llamo",self.__nombre,"y tengo",self.__edad,"años")

    def cumplir_anios(self):
        self.__edad += 1
        print("Ahora tengo",self.__edad,"años")

persona1 = Persona("Francisco Lozano", 27)
persona1.saludar()
persona1.cumplir_anios()
persona1.saludar()