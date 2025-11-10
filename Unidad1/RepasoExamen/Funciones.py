# Ejercicio 1: Crea una funcion con argumentos que reciba un nombre y varios titulos y los imprima
from sys import prefix


def funcionBiblioteca(nombre,* titulos):
    print("Nombre:",nombre,"- Titulos:",titulos)

funcionBiblioteca("Kevin","El beso con Marcos", "El coito con Marcos", "El divorcio con Marcos")


# Ejercicio 2: Crea una funcion clacularIva que te devuelva el precio sin iva, el precio con el iva del 21% y
# desempaquete los 2 valores retornados y los muestre con un f-String

def calcularIva(precio):
    precioConIva = precio * 1.21
    return precio, precioConIva

precio, precioConIva = calcularIva(10)
print(f"El precio sin iva es: {calcularIva(10)[0]} el precio con iva es {calcularIva(10)[1]:.2f}")
print(f"El precio sin iva es: {precio} el precio con iva es {precioConIva:.2f}")


# Ejercicio 3: Haz una funcion duplicar lista que reciba una lista como parametro y dentro de la funcion duplique la lista

def duplicarLista(lista):
    lista2 = lista.copy()
    # Metodo sin el copy
    # lista2 = list()
    # for i in lista:
    #     lista2.append(i)
    for i in range (0, len(lista2)):
        lista2[i] *= 2

    return lista2
lista = [1,2,3,4,5]

print(duplicarLista(lista))
print(lista)


# Ejercicio 4: Crea una funcion mostrarMenu que reciba un numero de opciones que imprima un menu numerado

def mostrarMenu(* opciones):
    contador = 0
    for i in opciones:
        contador += 1
        print("Opcion ",contador,") ",i,sep="")

mostrarMenu("Chupar pene", "Comer concha", "Jugar al LOL")


# Ejercicio 4: Crear una funcion mayorYMenor que reciba 3 numeros y retorne 2 cosas, el numero mayor y el menor

def mayorYMenor(num1, num2, num3):
    mayor = max(num1, num2, num3)
    menor = min(num1, num2, num3)
    return mayor, menor

print(f"El mayor es: {mayorYMenor(1,10,5)[0]} y el menor es {mayorYMenor(1,10,5)[1]}")


# Ejercicio 5: Crea una funcion login con 2 parametros con valores con valores por defectos y llamarla de
# 3 maneras difentes: sin argumentos, cambiando el primero y cambiando el segundo

def login(username = "kelvin", contraseña = "abcd1234"):
    return username, contraseña

print("Login: ",login())
print("Login: ",login(username="marcos"))
print("Login: ",login(contraseña="1234abcd"))


# Ejercicio 6: Pide 3 datos (nombre, edad, ciudad) por teclado y guardalos en una lista y pasalos a una funcion mostrarPerosna usando *lista

nombre = input("Introduce un nombre: ")
edad = int(input("Introduce una edad: "))
ciudad = input("Introduce una ciudad: ")
lista = [nombre, edad, ciudad]

def mostrarPersona(nombre, edad, ciudad):
    print(nombre, edad, ciudad, sep=", ")

mostrarPersona(*lista) # Si no se usa el * recibe una lista y crashea, poniendolo manda los datos 1 por 1


# Ejercicio 7: Haz una funcion promedios que calcule y retorne el promedio de todos los numeros que reciba

def promedios(* nums):
    suma = 0
    for i in range(0,len(nums)):
        suma += nums[i]
    return suma/len(nums)
lista = [7,5,4,6,8,9,10]

print(f"Resultado del promedio de {lista} es: {promedios(*lista):.2f}")


# Ejercicio 8: Haz una funcion cambiarPrimerElemento que reemplace el elemento 0 de la lista
# por el valor que se le pase y muestra el cambio fuera de la funcion

def cambiarPrimerElemento(lista, valor):
    lista[0] = valor
    return lista

lista = [1,2,3,4,5]
valor = 10
print(cambiarPrimerElemento(lista, valor))


# Ejercicio 9: Haz una funcion convertirAMayus que reciba un string y retorne ese string en maysculas usala dentro de un f-String

def convertirAMayusculas(palabra):
    palabraMayus = palabra.upper()
    return palabraMayus

palabra = "Kevin"
print(f"La palabra {palabra} en mayusculas es: {convertirAMayusculas(palabra)}")


# Ejercicio 10: Haz una funcion esPar que retorne True si es par y False si es impar y usala dentro de un f-String

def esPar(num):
    if num%2 == 0:
        return "Si"
    else:
        return "No"

num = 2
print(f"El numero {num} es par?: {esPar(num)}")
num = 77
print(f"El numero {num} es par?: {esPar(num)}")
