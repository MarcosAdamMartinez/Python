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
            case "Normal":
                if pokemonRival.__tipo in ["Roca", "Acero"]:
                    daño *= 0.5
                elif pokemonRival.__tipo == "Fantasma":
                    daño = 0

            case "Fuego":
                if pokemonRival.__tipo in ["Planta", "Hielo", "Bicho", "Acero"]:
                    daño *= 2
                elif pokemonRival.__tipo in ["Fuego", "Agua", "Roca", "Dragon"]:
                    daño *= 0.5

            case "Agua":
                if pokemonRival.__tipo in ["Fuego", "Tierra", "Roca"]:
                    daño *= 2
                elif pokemonRival.__tipo in ["Agua", "Planta", "Dragon"]:
                    daño *= 0.5

            case "Planta":
                if pokemonRival.__tipo in ["Agua", "Tierra", "Roca"]:
                    daño *= 2
                elif pokemonRival.__tipo in ["Fuego", "Planta", "Veneno", "Volador", "Bicho", "Dragon", "Acero"]:
                    daño *= 0.5

            case "Electrico":
                if pokemonRival.__tipo in ["Agua", "Volador"]:
                    daño *= 2
                elif pokemonRival.__tipo in ["Electrico", "Planta", "Dragon"]:
                    daño *= 0.5
                elif pokemonRival.__tipo == "Tierra":
                    daño = 0

            case "Hielo":
                if pokemonRival.__tipo in ["Planta", "Tierra", "Volador", "Dragon"]:
                    daño *= 2
                elif pokemonRival.__tipo in ["Fuego", "Agua", "Hielo", "Acero"]:
                    daño *= 0.5

            case "Lucha":
                if pokemonRival.__tipo in ["Normal", "Hielo", "Roca", "Siniestro", "Acero"]:
                    daño *= 2
                elif pokemonRival.__tipo in ["Veneno", "Volador", "Psiquico", "Bicho", "Hada"]:
                    daño *= 0.5
                elif pokemonRival.__tipo == "Fantasma":
                    daño = 0

            case "Veneno":
                if pokemonRival.__tipo in ["Planta", "Hada"]:
                    daño *= 2
                elif pokemonRival.__tipo in ["Veneno", "Tierra", "Roca", "Fantasma"]:
                    daño *= 0.5
                elif pokemonRival.__tipo == "Acero":
                    daño = 0

            case "Tierra":
                if pokemonRival.__tipo in ["Fuego", "Electrico", "Veneno", "Roca", "Acero"]:
                    daño *= 2
                elif pokemonRival.__tipo in ["Planta", "Bicho"]:
                    daño *= 0.5
                elif pokemonRival.__tipo == "Volador":
                    daño = 0

            case "Volador":
                if pokemonRival.__tipo in ["Planta", "Lucha", "Bicho"]:
                    daño *= 2
                elif pokemonRival.__tipo in ["Electrico", "Roca", "Acero"]:
                    daño *= 0.5

            case "Psiquico":
                if pokemonRival.__tipo in ["Lucha", "Veneno"]:
                    daño *= 2
                elif pokemonRival.__tipo in ["Psiquico", "Acero"]:
                    daño *= 0.5
                elif pokemonRival.__tipo == "Siniestro":
                    daño = 0

            case "Bicho":
                if pokemonRival.__tipo in ["Planta", "Psiquico", "Siniestro"]:
                    daño *= 2
                elif pokemonRival.__tipo in ["Fuego", "Lucha", "Veneno", "Volador", "Fantasma", "Acero", "Hada"]:
                    daño *= 0.5

            case "Roca":
                if pokemonRival.__tipo in ["Fuego", "Hielo", "Volador", "Bicho"]:
                    daño *= 2
                elif pokemonRival.__tipo in ["Lucha", "Tierra", "Acero"]:
                    daño *= 0.5

            case "Fantasma":
                if pokemonRival.__tipo in ["Psiquico", "Fantasma"]:
                    daño *= 2
                elif pokemonRival.__tipo == "Siniestro":
                    daño *= 0.5
                elif pokemonRival.__tipo == "Normal":
                    daño = 0

            case "Dragon":
                if pokemonRival.__tipo == "Dragon":
                    daño *= 2
                elif pokemonRival.__tipo == "Acero":
                    daño *= 0.5
                elif pokemonRival.__tipo == "Hada":
                    daño = 0

            case "Siniestro":
                if pokemonRival.__tipo in ["Psiquico", "Fantasma"]:
                    daño *= 2
                elif pokemonRival.__tipo in ["Lucha", "Siniestro", "Hada"]:
                    daño *= 0.5

            case "Acero":
                if pokemonRival.__tipo in ["Hielo", "Roca", "Hada"]:
                    daño *= 2
                elif pokemonRival.__tipo in ["Fuego", "Agua", "Electrico", "Acero"]:
                    daño *= 0.5

            case "Hada":
                if pokemonRival.__tipo in ["Lucha", "Dragon", "Siniestro"]:
                    daño *= 2
                elif pokemonRival.__tipo in ["Fuego", "Veneno", "Acero"]:
                    daño *= 0.5

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



