import random

# Ejercicio 11
# contador = 0
# iguales = False

# while iguales == False:
#     dado1 = random.randint(1, 6)
#     dado2 = random.randint(1, 6)
#     if dado1 == dado2:
#         iguales = True
#     print(dado1, " - ", dado2, end="\n")
#     contador += 1
# print("Veces que se han tirado: ",contador)

# Ejercicio 12
# i = int(input("Introduce el numero de dados que vas a tirar:\n"))
# j = int(input("Introduce el numero de caras del dado:\n"))
#
# while i != 0:
#     if i == 1:
#         print(random.randint(1,j))
#     else:
#         print(random.randint(1,j),end="-")
#     i = i - 1

# Ejercicio 13
# i = int(input("Introduce el numero de dados que vas a tirar:\n"))
# j = int(input("Introduce el numero de caras del dado:\n"))
#
#
# while i != 0:
#     if j % 2 == 0:
#         if i == 1:
#             print(random.randint(1,j))
#         else:
#             print(random.randint(1,j),end="-")
#         i = i - 1
#     else:
#         print("No se permiten dados con caras impares")
#         j = int(input("Introduce el numero de caras del dado:\n"))


# Ejercicio 14
# i = int(input("Introduce un numero:\n"))
# j = int(input("Introduce otro numero:\n"))
# print(random.randint(i,j))

# Ejercicio 15
# i = int(input("Introduce un numero:\n"))
# j = int(input("Introduce otro numero:\n"))
# if i < j:
#     print(random.randint(i,j))
# else: print(random.randint(j,i))

# Ejercicio 16
# for _ in range (0,6,1):
#     print(random.randint(1,49),end = " ")

# Ejercicio 17
# for _ in range (0,15,1):
#     i = random.randint(1,3)
#
#     if i == 1:
#         print(1)
#     elif i == 2:
#         print(2)
#     else:
#         print("X")

# Ejercicio 18
# i = 0
# j = 0
# while i != 666:
#     j = j+i
#     i = random.randint(1,1000)
# print("Restan",j,"dias para el apocalipsis!!!")

# Ejercicio 19
# i = int(input("Introduce un numero:\n"))
# j = 1
#
# for j in range(1,i,1):
#     if i % j == 0:
#         print(j)

# Ejercicio 20
# i = int(input("Introduce un numero:\n"))
# j = int(input("Introduce otro numero:\n"))
# k = int(input("Introduce un ultimo numero:\n"))
#
# if i >= j and i >= k:
#     mayor = i
#     if j >= k:
#         medio = j
#         menor = k
#     else:
#         medio = k
#         menor = j
# elif j >= i and j >= k:
#     mayor = j
#     if i >= k:
#         medio = i
#         menor = k
#     else:
#         medio = k
#         menor = i
# else:
#     mayor = k
#     if i >= j:
#         medio = i
#         menor = j
#     else:
#         medio = j
#         menor = i
#
# print("El mayor es", mayor, "el del medio", medio, "y el ultimo", menor)