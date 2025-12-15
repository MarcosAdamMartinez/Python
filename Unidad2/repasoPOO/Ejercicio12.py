# Crea las clases Profesor y Asignatura donde:
# Un profesor puede impartir varias asignaturas
# Una asignatura tiene un único profesor
# Requisitos:
# Al asignar un profesor a una asignatura, esta debe añadirse automáticamente a la lista del profesor
# Implementa __str__() en ambas clases
# Ejemplo de salida:
# Profesor: Ana → Asignaturas: Matemáticas, Física
# Asignatura: Matemáticas → Profesor: Ana
#
# 👉 Este ejercicio es MUY típico de examen DAM 2

class Profesor():
    def __init__(self, nombre, ):
        self.__nombre = nombre
        self.__asignaturas = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def asignaturas(self):
        return self.__asignaturas

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @asignaturas.setter
    def asignaturas(self, asignaturas):
        self.__asignaturas = asignaturas

    def añadir_asignatura(self, asignatura):
        if asignatura not in self.__asignaturas:
            self.__asignaturas.append(asignatura)

    def __str__(self):
        texto = f"Profesor: {self.nombre} | Asignaturas: "

        for asignatura in self.asignaturas:
            texto += asignatura.nombre + ", "

        return texto[:-2]



class Asignatura():
    def __init__(self, nombre, profesor):
        self.__nombre = nombre
        self.__profesor = profesor
        profesor.añadir_asignatura(self)

    @property
    def nombre(self):
        return self.__nombre

    @property
    def profesor(self):
        return self.__profesor

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @profesor.setter
    def profesor(self, profesor):
        self.__profesor = profesor

    def __str__(self):
        return f"Asignatura: {self.nombre} | Profesor: {self.profesor.nombre}"

profesor1 = Profesor("Ana")
asignatura1 = Asignatura("Matematicas", profesor1)
asignatura2 = Asignatura("Fisica", profesor1)

print(profesor1)
print(asignatura1)
print(asignatura2)