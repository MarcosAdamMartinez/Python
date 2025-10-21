import random

num = int(input("Escribe un numero: "))
numEsMayor = False
while not numEsMayor:
    if num >= 10:
        numEsMayor = True
        print("5 números pares comprendidos entre el 1 y el", num, ":")
        listaNums = list()
        numRand = random.randint(1, num)
        while len(listaNums) != 5:
            numRand = random.randint(1, num)
            if (numRand not in listaNums) and (numRand % 2 == 0):
                print(numRand)
                listaNums.append(numRand)
    else:
        num = int(input("Debes escribir un numero positivo mayor ol igual que 10: "))