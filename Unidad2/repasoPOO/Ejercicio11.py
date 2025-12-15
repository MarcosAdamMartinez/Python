# Crea una clase Alumno con:
# nombre
# nota
# Implementa:
# __str__() →
# Alumno: <nombre>, Nota: <nota>
#
# __eq__(self, other) → devuelve True si las notas son iguales
# __lt__(self, other) → compara alumnos por nota
# Desde el programa principal:
# Crea varios alumnos
# Ordénalos usando sorted()
# Muestra los alumnos ordenados
# 👉 Muy típico de examen DAM 2 (métodos mágicos + ordenación).


class Alumno():
    def __init__(self, nombre, nota):
        self.__nombre = nombre
        self.__nota = nota

    @property
    def nombre(self):
        return self.__nombre

    @property
    def nota(self):
        return self.__nota

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @nota.setter
    def nota(self, nota):
        self.__nota = nota

    def __str__(self):
        return f"Nombre: {self.nombre} | Nota: {self.nota}"

    def __eq__(self, otroAlumno):
        return self.nota == otroAlumno.nota

    def __lt__(self, otroAlumno):
        return self.nota < otroAlumno.nota

alumno1 = Alumno("Aitor", 1)
alumno2 = Alumno("Fran", 5)
alumno3 = Alumno("Marcos",10)
alumno4 = Alumno("Kevin",7)

listaAlumnos = [alumno1, alumno2, alumno3, alumno4]

lista_ordenada = sorted(listaAlumnos, reverse=True)

for alumno in lista_ordenada:
    print(alumno)
