# Crea las clases:
# Trabajador → atributos: nombre, salario
# Estudiante → atributos: nombre, carrera
# Becario → hereda de Trabajador y Estudiante
# Requisitos:
# Becario debe inicializar correctamente todos los atributos
# Implementa __str__() en cada clase para mostrar sus datos
# Desde el programa principal:
# Crea un becario y muestra sus datos
# 👉 Este ejercicio mezcla herencia múltiple + POO avanzada, típico de DAM 2.

class Trabajador():
    def __init__(self, nombre, salario):
        self.__nombre = nombre
        self.__salario = salario

    @property
    def nombre(self):
        return self.__nombre

    @property
    def salario(self):
        return self.__salario

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @salario.setter
    def salario(self, salario):
        self.__salario = salario


class Estudiante():
    def __init__(self, nombre, carrera):
        self.__nombre = nombre
        self.__carrera = carrera

    @property
    def nombre(self):
        return self.__nombre

    @property
    def carrera(self):
        return self.__carrera

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @carrera.setter
    def carrera(self, carrera):
        self.__carrera = carrera


class Becario(Trabajador, Estudiante):
    def __init__(self, nombre, salario, carrera):
        Trabajador.__init__(self, nombre, salario)
        Estudiante.__init__(self, nombre, carrera)

    def __str__(self):
        return f"Becario: {self.nombre} | Salario: {self.salario} | Carrera: {self.carrera}"


becario1 = Becario("Becario 1", 1500, "Ingenieria de Software")
print(becario1)