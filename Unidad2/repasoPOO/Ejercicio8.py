# Modifica las clases Vehiculo y Coche para que:
# Implementen el métodito especial __str__()
# El métodito __str__() devuelva exactamente lo mismo que descripcion()
# Desde el programa principal:
# Imprime los objetos directamente con print(objeto)
# NO llames a descripcion() explícitamente

class Vehiculo():
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo

    @property
    def marca(self):
        return self.__marca

    @property
    def modelo(self):
        return self.__modelo

    @marca.setter
    def marca(self, nuevaMarca):
        self.__marca = nuevaMarca

    @modelo.setter
    def modelo(self, nuevoModelo):
        self.__modelo = nuevoModelo

    def descripcion(self):
        return f"Marca: {self.marca} | Modelo: {self.modelo}"

    # def __str__(self):
    #     return f"Marca: {self.marca} | Modelo: {self.modelo}"

    def __str__(self):
        return self.descripcion()

class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.__puertas = puertas

    @property
    def puertas(self):
            return self.__puertas

    @puertas.setter
    def puertas(self, nuevasPuertas):
            self.__puertas = nuevasPuertas

    def descripcion(self):
        return f"Marca: {self.marca} | Modelo: {self.modelo} | Puertas: {self.puertas}"

    # def __str__(self):
    #     return f"Marca: {self.marca} | Modelo: {self.modelo} | Puertas: {self.puertas}"

    def __str__(self):
        return self.descripcion()


vehiculo1 = Vehiculo("Mercedes", "GLA200")
vehiculo2 = Vehiculo("Toyota", "Corolla")
coche1 = Coche( "BMW", "Serie-3 320-D",5)
coche2 = Coche( "Audi", "A4", 5)

listaVehiculos = [vehiculo1, coche2, coche1, vehiculo2]

for vehiculo in listaVehiculos:
    print(vehiculo)