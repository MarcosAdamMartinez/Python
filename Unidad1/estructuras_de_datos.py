lista = []
lista2 = list()

lista3 = [2,5,6,7,8,12,7]

lista4 = [34,"Pepe",False,7567.45,[1,2,3]]
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


print("\n")
print(lista3)
lista3.sort(reverse=True)
print(lista3)
