tupla = (1,2,3,4,5)
print(tupla)

print("\n")
tupla2 = ("Maria","Hola","Pepe")
print(tupla2)

print("\n")
tupla3 = (23, "Jose Maria", False, (1,2,3), 44.5, [1,2,3])
print(tupla3)

#Tupla vacia
print("\n")
tupla4 = ()
print(tupla4)

#Tupla con 1 unico valor
print("\n")
tupla5 = ("Sevilla",)
print(tupla5)

#Recorrer tupla
print("\n")
for elemento in tupla5:
    print(elemento)

print("\n")
for i in range(0, len(tupla5)):
    print(i, "-", tupla5[i])

#Transformar a lista
print("\n")
lista = list(tupla3)
print(lista)

#Transformar a cadena de texto
print("\n")
texto = str(tupla3)
print(texto)

#Transformar a tupla
print("\n")
tupla6 = tuple([1, 2, 3, 4, 5])
print(tupla6)
tupla7 = tuple("Hola Mundo")
print(tupla7)

#Otra forma de crear tuplas
tupla8 = "Pepe", "Juan", tupla6, "Ana"
print(tupla8)

#Mostrar por elemento - "Modificar" elementos en una tupla
# tupla8[1] = "Rocio"
print("\n")
print(tupla3)
tupla3[5][1] = 4
print("\n")
print(tupla3)

#If en tupla
print("\n")
if 4 in tupla:
    print("El 4 está en la tupla")
print("\n")
if 33 not in tupla:
    print("El 33 no está en la tupla")

profesor = ("Jose maria", "Morales", 57, False, True)

nombre, apellidos, edad, alumno, profe = profesor
print("\n")
print(apellidos, edad)