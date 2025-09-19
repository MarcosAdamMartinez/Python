import random

contador = 1

i = random.randint(1,6)
j = random.randint(1,6)
print(i," - ",j, end="\n")

while (i) != (j):
    i=random.randint(1,6)
    j=random.randint(1,6)
    print(i, " - ", j, end="\n")
    contador += 1
print("Veces que se han tirado: ",contador)