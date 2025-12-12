from abc import ABCMeta

class Persona(metaclass=ABCMeta):
    nombre = None
    apellido = None

class Alumno(Persona):
    def __init__(self,nombre, apellido, edad, ciclo, grupo):
        super.nombre = nombre
        super.apellido = apellido
        self.edad = edad
        self.ciclo = ciclo
        self.grupo = grupo
        if edad >= 18:
            self.esMayorEdad = True
        else:
            self.esMayorEdad = False

class Profesor:
    def __init__(self,nombre,apellido, grupoTutor="Ninguno", departamento=""):
        super.nombre = nombre
        super.apellido = apellido
        self.grupoTutor = grupoTutor
        if departamento in ["Informatica","Empresa","Ingles"]:
            self.departamento = departamento
        else:
            raise Exception("Departamento incorrecto")

class Ciclo:
    def __init__(self,nombre, modulos):
        self.nombre = nombre
        self.modulos = modulos

class Grupo(Profesor):
    def __init__(self,nombre, ciclo, curso, tutor, numeroAlumnos, listaAlumnos):
        super().grupoTutor = tutor
        self.nombre = nombre
        self.ciclo = ciclo
        self.curso = curso
        self.numeroAlumnos = numeroAlumnos
        self.listaAlumnos = listaAlumnos

class Modulo:
    def __init__(self,nombre, anno, horas, optativo):
        self.nombre = nombre
        self.anno = anno
        self.horas = horas
        self.optativo = optativo