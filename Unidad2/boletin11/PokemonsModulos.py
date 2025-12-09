from enum import Enum
import random

class Pokemon:
    def __init__(self,codigo,nombre,tipo):
        self.__codigo = codigo
        self.__nombre= nombre
        self.__tipo = tipo
        self.__evolucion = None
        self.salud = random.randint(50,100)

    def setEvolucion(self, pokemon):
        self.__evolucion = pokemon

    def evoluciona(self):
        evo = self
        if self.__evolucion == None:
            print("El Pokemon no ha evolucionado")
        else:
            evo = self.__evolucion

        return evo

    def mostrar(self):
        print(self.__nombre)

    def atacar(self, pokemonRival):
        daño = random.randint(0,35)
        match self.__tipo:
            case "Fuego":
                if pokemonRival.__tipo== "Planta" or pokemonRival.__tipo== "Acero" or pokemonRival.__tipo== "Bicho" or pokemonRival.__tipo== "Hielo":
                    daño *= 2
            case "Planta":
                if pokemonRival.__tipo== "Agua" or pokemonRival.__tipo== "Tierra" or pokemonRival.__tipo== "Roca":
                    daño *= 2
                elif pokemonRival.__tipo=="Volador" or pokemonRival.__tipo=="" or pokemonRival=="Fuego" or pokemonRival=="Acero":
                    daño *= 0.5
            case "Acero":
                if pokemonRival.__tipo== "Hielo" or pokemonRival.__tipo== "Roca" or pokemonRival.__tipo== "Psiquico":
                    daño *= 2
                elif pokemonRival.__tipo=="Agua" or pokemonRival.__tipo=="Electrico" or pokemonRival=="Fuego" or pokemonRival=="Acero":
                    daño *= 0.5
                elif pokemonRival.__tipo=="Veneno":
                    daño = 0

        pokemonRival.salud -= daño
        print(self.__nombre , "Ha atacado a", pokemonRival.__nombre , " y le quito " , daño , "de salud")
        print(pokemonRival.__nombre , "Tiene", pokemonRival.salud , "De salud")
        print("*****************")

    def combate(self, pokemonRival):
        print("--------------------------------------------------------------")
        print(self.__nombre, "Tiene" , self.salud , "Puntos de salud inical")
        print(pokemonRival.__nombre, "Tiene" , pokemonRival.salud , "Puntos de salud inical")
        print("--------------------------------------------------------------")
        print("")

        continuar = True

        mensaje = ""
        while continuar :
            self.atacar(pokemonRival)
            if pokemonRival.salud > 0:
                pokemonRival.atacar(self)
            else:
                mensaje =  "Ha ganado " + self.__nombre
                continuar = False

            if self.salud < 0:
                mensaje = "Ha ganado " + pokemonRival.__nombre
                continuar = False

        return mensaje

class Equipo:
    def __init__(self,codigo,nombreEquipo):
        self.__codigo = codigo


class PokemonLegendario:
    def __init__(self,codigo,nombre, tipo,nivel):
        self.__codigo = codigo







