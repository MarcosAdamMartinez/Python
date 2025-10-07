from operator import index
import random

lista = []
lista2 = list()

lista3 = [2,5,6,7,8,12,7,14,12,5,5]

lista4 = [34,"Pepe",False,7567.45,[1,2,3]]
listan = ["Jorge","Pepe","Ana","Manoli","Pilar"]
print(lista4)

print("\n")
for elemento in lista4:
    print(elemento)

#Recorremos la lista por su longitud
print("\n")
for posicion in range(0, len(lista4)):
    print(posicion,"-",lista4[posicion])

#Añadimos un elemento
print("\n")
lista4.append("Nuevo elemento")
print(lista4)

#Sumamos mas campos a la lista
print("\n")
lista5 = lista3 + [23.45]
print(lista5)

#Sumamos listas
print("\n")
lista6 = lista5 + lista4
print(lista6)

# lista3.extend(listan)

#Extrae el elemento de la posicion que especifiquemos y te lo muestra
print("\n")
print(lista3)
print(lista3.pop(1))
print(lista3)

#Busca el primer elemento que sea 7
print("\n")
lista3.remove(7)
print(lista3)

#Ordenamos la lista (Solo funciona con numeros y cadenas)
print("\n")
print(lista3)
lista3.sort()
print(lista3)

#Ordenamos la lista al reves(Solo funciona con numeros y cadenas)
print("\n")
print(lista3)
lista3.sort(reverse=True)
print(lista3)

#Añadir nuevo elemento a la posicion que especifiquemos
print("\n")
lista3.insert(-1,15)
print(lista3)

#Numero de veces que aparece un elemento en una lista (si no aparece devuelve 0)
print("\n")
print(lista3.count(5))

#Devuelve la posicion del primer dato que aparezca, si no existe devuelve una excepcion
print("\n")
print(lista3.index(5))

#Pasar lista a texto y texto a lista
texto = str(lista3)
print(texto)
texto2 = "Hola mundo"
lista7 = list(texto2)
print(lista7)

#Quitarle los []
print("\n")
texto = texto.replace("[","")
texto = texto.replace("]","")
print(texto)

#Crear matriz (lista de listas)
print("\n")
matriz = [[1,2,3],[4,5,6],[7,8,9]]
print(matriz[1][0])

#Cositas de listas
print("\n")
print(lista3)
print(lista3[:5])
print(lista3[2:5])
print(lista3[5:])
print(lista3[5::2])
print(lista3[::-1])

#Comporbar si un elemento esta en una lista
listax = [4,7,44,5,6,7,1]
listay = ["Maria","Juan","Pepe"]
print("\n")
if 4 in listax:
    print("4 si esta en la lista")

if 8 not in listax:
    print("8 no esta en la lista")

if "Jose" not in listay:
    print("\"Jose\" no esta en la lista")

#
#
#Metodos de la libreria random que se usan para listas
print("\n")
#Elige aleatoriamente
print(random.choice(listan))
#Elige 3 elementos de la lista sin repetir hasta que no queden
print(random.sample(listan,3))
#Cambia de posicion los valores de la lista aleatoriamente
random.shuffle(listan)
print(listan)

#
#
#Metodos para controlar cadenas mejor
print("\n")
cadena = "123"

if cadena.isalpha():
    print("Son letras")
else:
    print("Son numeros")

if cadena.isdigit():
    print("Son numeros")
else:
    print("No son numeros")

if cadena.isalnum():
    print("Es alfanumerico")
else:
    print("No es alfanumerico")
