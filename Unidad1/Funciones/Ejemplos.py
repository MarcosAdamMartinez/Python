# Escribir un programa que muestre por pantalla los 50 primeros números primos, sus
# raíces cuadradas, sus cuadrados y sus cubos
import math

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
#
# def funcionPrimos(n):
#     primos = []
#     num = 2
#     while len(primos) < n:
#         if es_primo(num):
#             primos.append(num)
#         num += 1
#     for p in primos:
#         print("Numero: ", p, "\tRaíz Cuadrada: ", round(math.sqrt(p), 2), "\tCuadrado: ", p ** 2, "\tCubo: ", p ** 3)
#
# primos = funcionPrimos(50)

def funcionParejaPrimos():
    primo = 0
    num = 50
    while primo < 50:
        if es_primo(num) and es_primo(num+2):
            primo = num
        num += 1
    return primo, primo+2

print(funcionParejaPrimos())