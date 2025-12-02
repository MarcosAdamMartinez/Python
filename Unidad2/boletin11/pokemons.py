import random


class Pokemon:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__pv = random.randint(50,100)
        self.evolucion = "No tiene evolucion"

    def setEvolucion(self,evolucion):
        self.evolucion = evolucion

    def evoluciona(self):

    def combateContra(self, contrincante):
        daño = random.randint(25, 100)
        contrincante.__pv -= daño
        if contrincante.__pv != 0:
            daño = random.randint(25, 100)
            self.__pv -= daño
            if self.__pv <= 0:
                print(self.__nombre,"ha sido derrotado")
            else:
                print("Ninguno de los 2 ha sido derrotado")
        else:
            print(self.__nombre,"ha ganado")


p1 = Pokemon("Pikachu")

p2 = Pokemon("Gengar")
p1.combateContra(p2)
