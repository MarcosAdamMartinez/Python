from tkinter.constants import CURRENT


class Empleado:
    def __init__(self, nombre, apellidos, edad):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__edad = edad # La doble _ nos permite "proteger" el atributo

    @property
    def edad(self):
        return self.__edad

    @property
    def nombre(self):
        return self.__nombre

    @property
    def apellidos(self):
        return self.__apellidos

    @edad.setter
    def edad(self, nuevaEdad):
        self.__edad = nuevaEdad

    @nombre.setter
    def nombre(self, nuevoNombre):
        self.__nombre = nuevoNombre

    @apellidos.setter
    def nombre(self, nuevosApellidos):
        self.__apellidos = nuevosApellidos

# El correcto uso de las funciones con __ es para sobreescribirlas en nuestras clases:
    # Creamos un str personalizado:
    def __str__(self):
        return self.apellidos+", "+self.nombre

# Podemos meter atributos fuera del constructor:
empleado1 = Empleado("Jose Maria","Morales Vazquez", 57)
empleado1.activo = True


print(empleado1.apellidos,empleado1.nombre,sep=", ")
print(empleado1.edad)

empleado1.edad = 58
print(empleado1.edad)

print(str(empleado1))


# Eliminar un objeto o variable:
del empleado1

x = 5
del x


class Cuenta:
    def __init__(self, titular, saldo):
        self.__titular = []
        self.__titular.append(titular)
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

    # Sobreescribimos el metodo add para sumar cuentas:
    def __add__(self, cuenta):
        self.saldo = self.saldo + cuenta.saldo
        self.titular = self.titular + cuenta.titular
        return self


c1 = Cuenta("Jose Maria Morales", 1000)
c2 = Cuenta("Javier Puche", 5000)

c1 = c1 + c2

print(c1.titular)
