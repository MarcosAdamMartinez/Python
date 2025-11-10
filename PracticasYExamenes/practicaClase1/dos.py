frase = input("Introduce una frase: ")
letra = input("Letra a mantener: ")
contador = 0
result = ""
nuevoResult = ""

if len(letra) == 1:

    for x in frase:
        if x == letra:
            result += x
        elif x == " ":
            result += " "
        else:
            result += "*"
    print("Resultado: ", result)

letra2 = input("Introduce una letra: ")

if len(letra2) == 1:
    for y in frase:
        if y == letra2:
            contador += 1
            nuevoResult += y
        elif y == letra:
            nuevoResult += y
        elif y == " ":
            nuevoResult += " "
        else:
            nuevoResult += "*"

    print("La letra", letra2, "aparece en", contador, "ocasiones")
    print("Resultado: ", nuevoResult, end="")