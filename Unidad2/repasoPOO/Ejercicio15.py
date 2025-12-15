# Crea un sistema de biblioteca con:
# Clases:
# Libro → atributos: titulo, autor, prestado (bool)
# Usuario → atributos: nombre, libros_prestados (lista)
# Biblioteca → mantiene listas de libros y usuarios
# Reglas:
# Métodito prestar_libro(usuario, libro):
# Solo si el libro no está prestado
# Añade el libro a usuario.libros_prestados
# Marca el libro como prestado
# Métodito devolver_libro(usuario, libro):
# Solo si el libro está prestado por ese usuario
# Quita el libro de usuario.libros_prestados
# Marca el libro como no prestado
# Métodito __str__() para cada clase mostrando su estado
# Desde el programa principal:
# Crea varios libros y usuarios
# Prueba prestar y devolver libros
# Muestra el estado final de la biblioteca y los usuarios

class Libro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        self.__prestado = False

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor

    @property
    def prestado(self):
        return self.__prestado

    @prestado.setter
    def prestado(self, valor):
        self.__prestado = valor

    def __str__(self):
        estado = "Prestado" if self.prestado else "Disponible"
        return f"Libro: {self.titulo} | Autor: {self.autor} | Estado: {estado}"


class Usuario:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__libros_prestados = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def libros_prestados(self):
        return self.__libros_prestados

    def añadir_libro(self, libro):
        self.__libros_prestados.append(libro)

    def quitar_libro(self, libro):
        if libro in self.__libros_prestados:
            self.__libros_prestados.remove(libro)

    def __str__(self):
        libros = ", ".join([libro.titulo for libro in self.libros_prestados])
        return f"Usuario: {self.nombre} | Libros prestados: {libros if libros else 'Ninguno'}"


class Biblioteca:
    def __init__(self):
        self.__libros = []
        self.__usuarios = []

    @property
    def libros(self):
        return self.__libros

    @property
    def usuarios(self):
        return self.__usuarios

    def añadir_libro(self, libro):
        self.__libros.append(libro)

    def añadir_usuario(self, usuario):
        self.__usuarios.append(usuario)

    def prestar_libro(self, usuario, libro):
        if libro.prestado:
            print(f"El libro '{libro.titulo}' ya está prestado")
        else:
            libro.prestado = True
            usuario.añadir_libro(libro)
            print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}")

    def devolver_libro(self, usuario, libro):
        if libro in usuario.libros_prestados:
            libro.prestado = False
            usuario.quitar_libro(libro)
            print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}")
        else:
            print(f"El libro '{libro.titulo}' no estaba prestado por {usuario.nombre}")

    def __str__(self):
        libros_texto = "\n".join(str(libro) for libro in self.libros)
        usuarios_texto = "\n".join(str(usuario) for usuario in self.usuarios)
        return f"=== Biblioteca ===\nLibros:\n{libros_texto}\n\nUsuarios:\n{usuarios_texto}"


# Programa principal

# Crear biblioteca
biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("1984", "George Orwell")
libro2 = Libro("El Quijote", "Miguel de Cervantes")
libro3 = Libro("Python para todos", "Al Sweigart")

# Añadir libros a la biblioteca
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)
biblioteca.añadir_libro(libro3)

# Crear usuarios
usuario1 = Usuario("Ana")
usuario2 = Usuario("Luis")

# Añadir usuarios a la biblioteca
biblioteca.añadir_usuario(usuario1)
biblioteca.añadir_usuario(usuario2)

# Pruebas de préstamo y devolución
biblioteca.prestar_libro(usuario1, libro1)
biblioteca.prestar_libro(usuario2, libro1)  # ya está prestado
biblioteca.prestar_libro(usuario2, libro2)

biblioteca.devolver_libro(usuario1, libro1)
biblioteca.devolver_libro(usuario2, libro1)  # no estaba prestado por Luis
biblioteca.prestar_libro(usuario2, libro1)

# Mostrar estado final
print("\nEstado final de la biblioteca:")
print(biblioteca)