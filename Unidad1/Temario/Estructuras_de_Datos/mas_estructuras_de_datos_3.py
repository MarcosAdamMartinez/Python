lista = ["Ana", "Pedro", "Luis"]
#Recorrer lista:
for nombre in lista:
    print(nombre)

#Recorrer lista con indice:
print("\n")
for i in range(len(lista)):
    print(i,"-", lista[i])

#Recorrer lista con indice y valor:
print("\n")
for i, nombre in enumerate(lista):
    print(i,"-",nombre)

#Hacer copias de listas:
print("\n")
numero1 = [14, 7]
numero2 = numero1.copy()
numero2[0] = numero2[0] * 2
print(numero2)
print(numero1)

def miFuncion(lista):
    lista[0] = lista[0] * 2
    print(lista)

miFuncion(numero1.copy())
print(numero1)