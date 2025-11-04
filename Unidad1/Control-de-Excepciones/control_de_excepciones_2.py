# Excepciones creadas por nosotros:ZeroDivisionError("No has dividido por 0 pero lo digo yo")

# n = int(input("Introduce un numero entero positivo: "))
# if n < 0:
#     raise Exception("No es un entero positivo")
# print(n)
#
# linea = input("Introduce el nombre de alguien feo: ")
# if linea == "Aitor":
#     raise Exception("Aitor es demasiado guapo como para que digas eso")
# print(linea)

# Excepcion forzada
# n = int(input("Introduce un numero entero positivo: "))
# raise ZeroDivisionError("No has dividido por 0 pero lo digo yo")

# Excepcion de booleanos (antigua pero util):
n = int(input("Introduce un numero entero positivo: "))
assert n>0 and n!=5, "El numero es negativo o igual a 5"