
# Elementos clave - valor, no pueden haber duplicados, si los hay se sobreescribe el primer valor:
diccionario = { "Nombre":"Sara", "Edad" : 57, "Solterx":True, "Edad" : 33 }

# Mostrar el diccionario entero y un valor (por clave) especifico:
print(diccionario)
print(diccionario["Edad"])

# Al recorrer el diccionario, devuelve las claves, para mostrar el elemento usamos la misma sintaxis de antes:
for elemento in diccionario:
    print(elemento, end=": ")
    print(diccionario[elemento])

# Otra manera de recorrer el diccionario:
for clave, valor in diccionario.items():
    print(clave,": ",valor)

# Los diccionarios funcionan con listas, esto nos permite "almacenar" varios valores en la misma clave:
diccionarioListas = { "Pokedex" : [] }
diccionarioListas["Pokedex"].append("Charmander")
diccionarioListas["Pokedex"].append("Charmeleon")
diccionarioListas["Pokedex"].append("Charizard")

for elemento in diccionarioListas["Pokedex"]:
    print(elemento, end=" ")
print()

# El metodo get es equivalente a usar [], el cambio es que al usar get, si la clave no existe no genera excepcion:
print(diccionario.get("Edad"))
print(diccionario.get("Edad2"))

# Asignar valores nuevos (si ponemos una clave que no exista en el diccionario se crea una nueva entrada):
diccionario["Edad"] = 44
diccionario["Altura"] = 1.92
print(diccionario.get("Edad"))
print(diccionario)

# Eliminar completamente el diccionario:
diccionario.clear()
print(diccionario)


# Otra manera de crear un diccionario:

dicc2 = dict(Primero = 'Uno', Tercero = 'Tres')
dicc2["Segundo"] = "Dos"
print(dicc2)

dicc3 = {}
dicc4 = dict()

