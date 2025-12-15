# Crea un sistema de gestión de biblioteca usando diccionarios:
# Diccionario libros → cada clave es el título y el valor es otro diccionario con:
# "autor" → autor del libro
# "prestado" → True/False
# Diccionario usuarios → cada clave es el nombre del usuario y el valor es la lista de títulos que tiene prestados
# Funciones:
# prestar_libro(usuario, titulo):
# Solo si el libro no está prestado
# Añade el título a la lista de libros del usuario
# Marca el libro como prestado
# devolver_libro(usuario, titulo):
# Solo si el usuario tiene el libro
# Quita el título de su lista
# Marca el libro como no prestado
# Desde el programa principal:
# Crea al menos 3 libros y 2 usuarios
# Prueba prestar y devolver libros
# Muestra el estado final de libros y usuarios

libros = {
    "Harry Potter y La Piedra Filosofal": {
            "autor": "J. K. Rowling",
            "prestado": False
        },
    "Harry Potter y El Caliz de Fuego": {
        "autor": "J. K. Rowling",
        "prestado": False
    },
    "Harry Potter y El Prisionero De Azkaban": {
        "autor": "J. K. Rowling",
        "prestado": False
    }
}

usuarios = {
    "Fran": [],
    "Kevin": []
}

def prestar_libro(usuario, titulo):
    if libros[titulo]["prestado"] == False:
        usuarios[usuario].append(titulo)
        libros[titulo]["prestado"] = True

def devolver_libro(usuario, titulo):
    if libros[titulo]["prestado"] == True:
        usuarios[usuario].remove(titulo)
        libros[titulo]["prestado"] = False

prestar_libro("Fran","Harry Potter y La Piedra Filosofal")
prestar_libro("Kevin","Harry Potter y El Caliz de Fuego")
print(usuarios)
devolver_libro("Fran","Harry Potter y La Piedra Filosofal")
prestar_libro("Kevin","Harry Potter y La Piedra Filosofal")
prestar_libro("Fran","Harry Potter y El Prisionero De Azkaban")
print(usuarios)
