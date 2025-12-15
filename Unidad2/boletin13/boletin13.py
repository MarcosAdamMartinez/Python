class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def get_nombre_completo(self):
        return self.nombre + " " + self.apellido


class Alumno(Persona):
    def __init__(self, nombre, apellido, edad, ciclo, grupo=None):
        Persona.__init__(self, nombre, apellido, edad)
        self.ciclo = ciclo
        self.grupo = grupo
        self.mayor_edad = edad >= 18

    def mostrar(self):
        print(self.get_nombre_completo(), ", Edad:", self.edad, ", Mayor de edad:", self.mayor_edad)


class Profesor(Persona):
    def __init__(self, nombre, apellido, departamento, grupo_tutor=None):
        Persona.__init__(self, nombre, apellido, 0)
        self.departamento = departamento
        self.grupo_tutor = grupo_tutor

    def mostrar(self):
        if self.grupo_tutor:
            tutor = self.grupo_tutor.nombre
        else:
            tutor = "Ninguno"
        print(self.get_nombre_completo(), ", Departamento:", self.departamento, ", Tutor de:", tutor)


class Modulo:
    def __init__(self, nombre, año, horas_semana, optativo):
        self.nombre = nombre
        self.año = año
        self.horas_semana = horas_semana
        self.optativo = optativo

    def mostrar(self):
        tipo = "Optativo"
        if not self.optativo:
            tipo = "Obligatorio"
        print(self.nombre, "(Año", self.año, ",", self.horas_semana, "h/semana,", tipo, ")")


class Ciclo:
    def __init__(self, nombre, tipo, modulos):
        self.nombre = nombre
        self.tipo = tipo
        self.modulos = modulos  # lista de objetos Modulo

    def mostrar(self):
        print("Ciclo:", self.nombre, "(", self.tipo, ")")
        print("Módulos:")
        for modulo in self.modulos:
            print(" -", end=" ")
            modulo.mostrar()


class Grupo:
    def __init__(self, nombre, ciclo, curso, tutor=None):
        self.nombre = nombre
        self.ciclo = ciclo
        self.curso = curso
        self.tutor = tutor
        self.alumnos = []  # lista vacía de alumnos

    def añadir_alumno(self, alumno):
        if alumno not in self.alumnos:
            self.alumnos.append(alumno)
            alumno.grupo = self
        else:
            print("El alumno", alumno.get_nombre_completo(), "ya está en el grupo.")

    def eliminar_alumno(self, alumno):
        if alumno in self.alumnos:
            self.alumnos.remove(alumno)
            alumno.grupo = None
        else:
            print("El alumno", alumno.get_nombre_completo(), "no se encuentra en el grupo.")

    def listar_informacion(self):
        print("Grupo:", self.nombre, ", Curso:", self.curso, ", Ciclo:", self.ciclo.nombre)
        if self.tutor:
            print("Tutor:", self.tutor.get_nombre_completo())
        else:
            print("Tutor: Ninguno")
        print("Número de alumnos:", len(self.alumnos))
        print("Alumnos matriculados:")
        for alumno in self.alumnos:
            print(" -", end=" ")
            alumno.mostrar()
        print("Módulos impartidos en este grupo:")
        for modulo in self.ciclo.modulos:
            print(" -", end=" ")
            modulo.mostrar()


# Módulos
mod1 = Modulo("Programación", 1, 5, False)
mod2 = Modulo("Bases de Datos", 1, 4, False)
mod3 = Modulo("Redes", 2, 3, True)

# Ciclo
ciclo_dam = Ciclo("DAM", "Grado Superior", [mod1, mod2, mod3])

# Profesor
prof1 = Profesor("Laura", "Gómez", "Informática")

# Grupo
grupo1 = Grupo("DAM1", ciclo_dam, 1, tutor=prof1)

# Alumnos
alumno1 = Alumno("Juan", "Pérez", 19, ciclo_dam)
alumno2 = Alumno("Ana", "López", 17, ciclo_dam)

# Añadir alumnos
grupo1.añadir_alumno(alumno1)
grupo1.añadir_alumno(alumno2)

# Listar información del grupo
grupo1.listar_informacion()
