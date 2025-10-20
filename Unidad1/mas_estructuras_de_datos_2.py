conjunto = {1, 2, 3, 4, 5}
print(conjunto)


print("\n")
profesPrimero = {"Ana", "Juan Carlos", "Sancho", "Natalia"}
print(profesPrimero)

print("\n")
profesSegundo = set(["Agustin", "Ana", "Natalia", "Javier", "Jose Maria"])
print(profesSegundo)

if "Juan Carlos" in profesPrimero:
    print("Juan Carlos da clases en primero")

if "Javier" not in profesPrimero:
    print("Javier no da clases en primero")

for elemento in profesPrimero:
    print(elemento)

print("\n")
print(len(profesPrimero))

# for i in range(0, len(profesPrimero)):
#     Esto no funciona porque los conjuntos no guardan un orden
#     print(profesPrimero[i])

#Añadir nuevo elemento
print("\n")
profesSegundo.add("Eduardo")
# Si añades un elemento duplicado no cambia nada
# profesSegundo.add("Eduardo")
print(profesSegundo)

#Eliminar elementos
print("\n")
profesSegundo.remove("Eduardo")
print(profesSegundo)
# Si eliminas un elemento que no existe salta error
# profesSegundo.remove("Eduardo")

#Sustraer un elemento (al azar)
print("\n")
profe = profesPrimero.pop()
print(profe)
print(profesPrimero)

#Limpiar el conjunto
# print("\n")
# profesPrimero.clear()
# print(profesPrimero)

#Converiones
conjunto1 = set([1,2,3,2,2,4,4,4,5,1,6,5])
print("\n")
print(conjunto1)

print("\n")
conjunto2 = set("Hola mundo cruel")
print(conjunto2)

print("\n")
lista = list(profesSegundo)
print(lista)
tupla = tuple(profesSegundo)
print(tupla)
texto = str(profesSegundo)
print(texto)

#Union
print("\n UNION:")
print(profesPrimero | profesSegundo)
print(profesPrimero.union(profesSegundo))


#Interseccion
print("\n INTERSECCION:")
print(profesPrimero & profesSegundo)
print(profesPrimero.intersection(profesSegundo))

#Diferencia
print("\n DIFERENCIA")
print(profesPrimero - profesSegundo)
print(profesPrimero.difference(profesSegundo))

#Exclusive OR
print("\n DIFERENCIA SIMETRICA:")
print(profesPrimero ^ profesSegundo)
print(profesPrimero.symmetric_difference(profesSegundo))