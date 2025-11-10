import random

print("10 números entre el 1 y el 1000")
listaNums = list()
contPares = 0
contImpares = 0

for i in range (0,10):
    numRand = random.randint(1,1000)
    listaNums.append(numRand)

listaTexto = str(listaNums)
listaTexto = listaTexto.replace("[","")
listaTexto = listaTexto.replace("]","")

print(listaTexto)

for i in range(0,len(listaNums)):
    if (listaNums[i] % 2) == 0:
        contPares += 1
    else:
        contImpares += 1

print("He generado",contPares,"números pares y",contImpares,"números impares")
print("EL número mayor ha sido el",max(listaNums),"y el menor",min(listaNums))