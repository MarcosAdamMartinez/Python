import random

contador = 0

# dado1 = random.randint(1, 6)
# dado2 = random.randint(1, 6)
iguales = False

# print(dado1, " - ", dado2, end="\n")

# while (dado1) != (dado2):

while iguales == False:
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    if dado1 == dado2:
        iguales = True
    print(dado1, " - ", dado2, end="\n")
    contador += 1
print("Veces que se han tirado: ",contador)