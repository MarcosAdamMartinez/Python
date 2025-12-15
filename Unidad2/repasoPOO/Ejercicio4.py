# Crea una clase CuentaBancaria que tenga:
# Atributos privados:
# titular
# saldo
# Métodos:
# mostrar_datos() → muestra:
#   Titular: <titular> | Saldo: <saldo> €
# ingresar(cantidad) → suma la cantidad al saldo
# retirar(cantidad) → resta la cantidad al saldo solo si hay saldo suficiente, si no:
# Saldo insuficiente
# Desde el programa principal:
# Crea una cuenta con saldo inicial 100
# Ingresa 50
# Retira 30
# Intenta retirar 200
# Muestra los datos finales

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @titular.setter
    def titular(self, nuevoTitular):
        self.__titular = nuevoTitular

    @saldo.setter
    def saldo(self, nuevoSaldo):
        self.__saldo = nuevoSaldo

    def mostrar_datos(self):
        print("Titular:",self.titular,"| Saldo: ",self.saldo," €")

    def ingresar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if self.saldo - cantidad < 0:
            print("Saldo insuficiente para la retirada")
        else:
            self.saldo -= cantidad


cuenta1 = CuentaBancaria("Fran",100)
cuenta1.ingresar(50)
cuenta1.retirar(30)
cuenta1.retirar(200)
cuenta1.mostrar_datos()
