from itertools import count

frase = input("Introduce una frase: ")
letra = input("Letra a mantener: ")
contador = 0
result = ""
resultFin = ""

if len(letra) == 1:

    for x in frase:
        if x == letra:
            result += x
            resultFin += x
        elif x == " ":
            result += " "
        else:
            result += "*"
    print("Resultado: ", result)

while result.count("*") != 0:
    nuevoResult = ""
    letra2 = input("Introduce una letra: ")
    if len(letra2) == 1:
        for y in frase:
            if y == letra2:
                contador += 1
                nuevoResult += y
                resultFin += y
            elif y == letra:
                nuevoResult += y
            elif y == " ":
                nuevoResult += " "
            else:
                nuevoResult += "*"

    print("La letra", letra2, "aparece en", contador, "ocasiones")
    print("Resultado: ", resultFin)
    contador = 0

print("Has ganado. Has necesitado",contador,"intentos para completar la frase")