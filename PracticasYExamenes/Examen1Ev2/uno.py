import datetime
from abc import ABCMeta, abstractmethod


class Conductor:
    def __init__(self, nombre, nif, annoNaciemiento, annoCarnet, puntosCarnet):
        self.__nombre = nombre
        self.__nif = nif
        self.__annoNaciemiento = annoNaciemiento
        self.__annoCarnet = annoCarnet
        self.__puntosCarnet = puntosCarnet

    @property
    def puntosCarnet(self):
        return self.__puntosCarnet

    @property
    def annoNaciemiento(self):
        return self.__annoNaciemiento

    @property
    def annoCarnet(self):
        return self.__annoCarnet

    @property
    def nombre(self):
        return self.__nombre

class Vehiculo(metaclass=ABCMeta):
    def __init__(self, matricula, annoVenta):
        self.__matricula = matricula
        self.__annoVenta = annoVenta

    @property
    def annoVenta(self):
        return self.__annoVenta

    @property
    def matricula(self):
        return self.__matricula

    def calcularSeguro(self, tipoSeguro):
        pass

class Moto(Vehiculo, Conductor):
    tipoSeguroValido = ["A terceros"]

    def __init__(self, matricula, annoVenta, conductor):
        super().__init__(matricula, annoVenta)
        self.__conductor = conductor

    @property
    def conductor(self):
        return self.__conductor


    def calcularSeguro(self, tipoSeguro):
        costoSeguro = 0

        if tipoSeguro in self.tipoSeguroValido:
            costoSeguro = 200 * (datetime.datetime.now().year-self.annoVenta)
            if self.conductor.puntosCarnet < 8:
                costoSeguro += 100
            if (datetime.datetime.now().year - self.conductor.annoNaciemiento) < 24:
                costoSeguro += 25
            if (datetime.datetime.now().year - self.conductor.annoCarnet) < 2:
                costoSeguro += 50
        else:
            costoSeguro = "No se hacen seguros a todo riesgo en motos"

        return costoSeguro

    def __str__(self):
        annosEdad = datetime.datetime.now().year - self.conductor.annoNaciemiento
        annosCarnet = datetime.datetime.now().year - self.conductor.annoCarnet
        return (f"Vehiculo: moto. Matricula: {self.matricula}. Año de compra: {self.annoVenta}\n"
                f"Conductor: {self.conductor.nombre}. Edad: {annosEdad}. Años de carnet: {annosCarnet}. Puntos: {self.conductor.puntosCarnet}\n"
                f"Precio del seguro a terceros: {self.calcularSeguro("A terceros")}\n"
                f"{self.calcularSeguro("A todo tiesgo")}")

class Coche(Vehiculo):
    tiposSegurosValidos = ["A todo riesgo", "A terceros"]

    def __init__(self, matricula, annoVenta, conductor):
        super().__init__(matricula, annoVenta)
        self.__conductor = conductor

    @property
    def conductor(self):
        return self.__conductor

    def calcularSeguro(self, tipoSeguro):
        costoSeguro = 0

        if tipoSeguro in self.tiposSegurosValidos:
            if tipoSeguro == "A terceros":
                costoSeguro = 250 * (datetime.datetime.now().year - self.annoVenta)
                if self.conductor.puntosCarnet < 8:
                    costoSeguro += 100
                if (datetime.datetime.now().year - self.conductor.annoNaciemiento) < 24:
                    costoSeguro += 50
                if (datetime.datetime.now().year - self.conductor.annoCarnet) < 2:
                    costoSeguro += 75

            elif tipoSeguro == "A todo riesgo":
                if (datetime.datetime.now().year-self.annoVenta+1) == 1:
                    costoSeguro = 400
                elif (datetime.datetime.now().year-self.annoVenta+1) == 2:
                    costoSeguro = 500
                elif (datetime.datetime.now().year-self.annoVenta+1) == 3:
                    costoSeguro = 700
                elif (datetime.datetime.now().year-self.annoVenta+1) > 3:
                    costoSeguro = 250 * (datetime.datetime.now().year-self.annoVenta)
                if self.conductor.puntosCarnet < 8:
                    costoSeguro += 100

        return costoSeguro

    def __str__(self):
        annosEdad = datetime.datetime.now().year - self.conductor.annoNaciemiento
        annosCarnet = datetime.datetime.now().year - self.conductor.annoCarnet
        return (f"Vehiculo: coche. Matricula: {self.matricula}. Año de compra: {self.annoVenta}\n"
                f"Conductor: {self.conductor.nombre}. Edad: {annosEdad}. Años de carnet: {annosCarnet}. Puntos: {self.conductor.puntosCarnet}\n"
                f"Precio del seguro a todo riesgo: {self.calcularSeguro("A todo riesgo")}\n"
                f"Precio del seguro a terceros: {self.calcularSeguro("A terceros")}\n")

conductor1 = Conductor("Jose María Morales","76574832D",1968,1986, 10)
conductor2 = Conductor("Ines Perado","76577832X",2007,2024, 8)

coche = Coche("6310NXB", 2024, conductor1)

moto = Moto("6310NXB", 2024, conductor2)

print(coche)
print(moto)