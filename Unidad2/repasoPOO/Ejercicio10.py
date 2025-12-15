# Crea una clase abstracta llamada Figura usando abc que tenga:
# Un métodito abstracto area()
# Crea dos clases que hereden de Figura:
# Rectangulo (base, altura)
# Circulo (radio)
# Cada una debe implementar el métodito area().
# Desde el programa principal:
# Crea una lista de figuras
# Recorre la lista mostrando el área de cada una
# 👉 Esto es examen puro de DAM 2 (clases abstractas + polimorfismo).

from abc import abstractmethod, ABCMeta
import math as m

class Figura(metaclass=ABCMeta):
    @abstractmethod
    def area(self):
        pass

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    @property
    def base(self):
        return self.__base

    @property
    def altura(self):
        return self.__altura

    @base.setter
    def base(self, base):
        self.__base = base

    @altura.setter
    def altura(self, altura):
        self.__altura = altura

    def area(self):
        return self.__base * self.__altura

class Circulo(Figura):
    def __init__(self, radio):
        self.__radio = radio

    @property
    def radio(self):
        return self.__radio

    @radio.setter
    def radio(self, radio):
        self.__radio = radio

    def area(self):
        return round((m.pi * (self.__radio ** 2)),2)

rectangulo1 = Rectangulo(3.0, 2.0)
rectangulo2 = Rectangulo(6.0, 4.0)
rectangulo3 = Rectangulo(2.0, 8.0)

circulo1 = Circulo(3.0)
circulo2 = Circulo(5.0)
circulo3 = Circulo(2.0)

listaFiguras = [rectangulo1, rectangulo2, rectangulo3, circulo1, circulo2, circulo3]

for figura in listaFiguras:
    print(figura.area())