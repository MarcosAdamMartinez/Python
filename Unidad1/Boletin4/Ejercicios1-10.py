#2. En matemáticas, la sucesión de Fibonacci se trata de una serie infinita de números
# naturales. Los dos primeros son siempre el 0 y el 1. Los siguientes se obtienen
# sumando los dos anteriores. El tercero sería 1 (la suma de 0 + 1), el cuarto sería 2 (la
# suma de 1 + 1), el quinto 3 (la suma de 1 + 2) y así sucesivamente. La lista con los 10
# primeros números sería esta: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34].

# Queremos hacer un programa que reciba un número por teclado y nos calcule tantos
# números de la sucesión de fibonacci como indique ese número. Por ejemplo, si
# metemos un 8 la salida de tu programa debería de ser así:
# 0,1,1,2,3,5,8,13

# numIt = int(input("Introduce un numero para que la sucesion llegue a el:"))
# fibon = [0,1]
#
# if numIt == 1:
#     fibon.pop()
# elif numIt == 0:
#     fibon = []
# else:
#     for _ in range (2,numIt):
#         fibon.append((fibon[-1]+fibon[-2]))
#     print(fibon)

# Escribir un programa que cuente el número de cifras que tiene un número (por
# ejemplo, el 8 tiene una cifra, el 221 tres y el 456789 seis).
# numero = 95
# numeroATexto = str(numero)
# print("El numero",numero,"tiene",len(numeroATexto),"cifras")

#Decimos que dos números primos son gemelos cuando están separados por un único
# número (el 11 y el 13, el 17 y el 19, el 41 y el 43, etc.). Escribir un programa que calcule
# la primera pareja de primos gemelos por encima del 50.