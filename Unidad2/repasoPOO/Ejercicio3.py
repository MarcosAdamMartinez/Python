# Modifica la clase Persona para que:
# Añadas getters para:
# nombre
# edad
#
# Desde el programa principal:
# Muestra por pantalla el nombre y la edad usando los getters, no accediendo directamente a los atributos

class Persona():
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    def saludar(self):
        print("Hola, me llamo",self.__nombre,"y tengo",self.__edad,"años")

    def cumplir_anios(self):
        self.__edad += 1
        print("Ahora tengo",self.__edad,"años")

persona1 = Persona("Francisco Lozano", 27)
print("Hola, me llamo",persona1.nombre,"y tengo",persona1.edad,"años")
persona1.cumplir_anios()
print("Hola, me llamo",persona1.nombre,"y tengo",persona1.edad,"años")